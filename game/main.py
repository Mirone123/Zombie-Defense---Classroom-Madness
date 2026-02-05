import sys
from enum import Enum, auto

import pygame

import database
import storage
from enemy import Zombie
from player import Player
from projectile import Projectile
from ui import draw_game_over, draw_hud, draw_menu, draw_name_input


class GameState(Enum):
    MENU = auto()
    NAME_INPUT = auto()
    PLAYING = auto()
    GAME_OVER = auto()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Zombie Defense - Classroom Madness")

        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.world_rect = self.screen.get_rect()

        database.init_db()

        self.state = GameState.MENU
        self.menu_selection = 0

        self.player_name = ""
        self.name_input = ""
        self.score_saved = False

        self.player = Player(self.width / 2, self.height / 2)
        self.zombies: list[Zombie] = []
        self.projectiles: list[Projectile] = []

        self.kills = 0
        self.survival_time = 0.0
        self.spawn_timer = 0.0
        self.spawn_interval = 1.1

        self.shoot_cooldown = 0.18
        self.shoot_timer = 0.0

        self.leaderboard_lines = self.get_leaderboard_lines()

    def reset_game(self):
        self.player.reset(self.width / 2, self.height / 2)
        self.zombies.clear()
        self.projectiles.clear()
        self.kills = 0
        self.survival_time = 0.0
        self.spawn_timer = 0.0
        self.spawn_interval = 1.1
        self.shoot_timer = 0.0
        self.score_saved = False

    @staticmethod
    def get_leaderboard_lines() -> list[str]:
        db_rows = database.get_leaderboard(5)
        if db_rows:
            return [storage.format_score_line(row) for row in db_rows]
        return storage.get_leaderboard_lines(5)

    def persist_result(self):
        if self.score_saved:
            return

        clean_name = self.player_name.strip() or "Hrac"
        storage.save_score(clean_name, self.kills)
        database.save_match_result(clean_name, self.kills, self.survival_time)
        self.leaderboard_lines = self.get_leaderboard_lines()
        self.score_saved = True

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if self.state == GameState.MENU:
                self.handle_menu_event(event)
            elif self.state == GameState.NAME_INPUT:
                self.handle_name_input_event(event)
            elif self.state == GameState.PLAYING:
                self.handle_playing_event(event)
            elif self.state == GameState.GAME_OVER:
                self.handle_game_over_event(event)

    def handle_menu_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.menu_selection = (self.menu_selection - 1) % 2
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.menu_selection = (self.menu_selection + 1) % 2
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                if self.menu_selection == 0:
                    self.name_input = self.player_name
                    self.state = GameState.NAME_INPUT
                else:
                    self.quit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.Vector2(event.pos)
            start_rect = pygame.Rect(0, 0, 200, 40)
            start_rect.center = (self.width // 2, self.height // 2)
            quit_rect = pygame.Rect(0, 0, 200, 40)
            quit_rect.center = (self.width // 2, self.height // 2 + 50)
            if start_rect.collidepoint(mouse_pos):
                self.name_input = self.player_name
                self.state = GameState.NAME_INPUT
            elif quit_rect.collidepoint(mouse_pos):
                self.quit_game()

    def handle_name_input_event(self, event: pygame.event.Event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_RETURN:
            self.player_name = self.name_input.strip() or "Hrac"
            self.reset_game()
            self.state = GameState.PLAYING
        elif event.key == pygame.K_ESCAPE:
            self.state = GameState.MENU
        elif event.key == pygame.K_BACKSPACE:
            self.name_input = self.name_input[:-1]
        elif event.unicode and event.unicode.isprintable() and len(self.name_input) < 20:
            self.name_input += event.unicode

    def handle_playing_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.state = GameState.MENU

    def handle_game_over_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.name_input = self.player_name
                self.state = GameState.NAME_INPUT
            elif event.key == pygame.K_m:
                self.state = GameState.MENU
            elif event.key == pygame.K_ESCAPE:
                self.quit_game()

    def get_movement_input(self) -> pygame.Vector2:
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction.x += 1

        return direction

    def should_fire(self) -> bool:
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed(3)
        return mouse_buttons[0] or keys[pygame.K_SPACE]

    def fire_projectile(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        direction = mouse_pos - self.player.position
        self.projectiles.append(Projectile(self.player.position, direction))

    def update(self, dt: float):
        if self.state != GameState.PLAYING:
            return

        self.survival_time += dt
        self.spawn_timer += dt
        self.shoot_timer = max(0.0, self.shoot_timer - dt)

        input_vector = self.get_movement_input()
        self.player.update(dt, input_vector, self.world_rect)

        if self.should_fire() and self.shoot_timer == 0:
            self.fire_projectile()
            self.shoot_timer = self.shoot_cooldown

        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.zombies.append(Zombie.spawn_at_screen_edge(self.world_rect))
            self.spawn_interval = max(0.35, self.spawn_interval * 0.99)

        for zombie in self.zombies:
            zombie.update(dt, self.player.position)

        for projectile in self.projectiles:
            projectile.update(dt)

        self.handle_collisions()
        self.projectiles = [p for p in self.projectiles if not p.is_out_of_bounds(self.world_rect)]

        if not self.player.is_alive:
            self.persist_result()
            self.state = GameState.GAME_OVER

    def handle_collisions(self):
        remaining_projectiles: list[Projectile] = []
        for projectile in self.projectiles:
            hit_zombie = None
            for zombie in self.zombies:
                if projectile.position.distance_to(zombie.position) <= projectile.radius + zombie.radius:
                    hit_zombie = zombie
                    break
            if hit_zombie:
                self.zombies.remove(hit_zombie)
                self.kills += 1
            else:
                remaining_projectiles.append(projectile)
        self.projectiles = remaining_projectiles

        damage_cooldown = []
        for zombie in self.zombies:
            if zombie.position.distance_to(self.player.position) <= zombie.radius + self.player.radius:
                damage_cooldown.append(zombie)

        if damage_cooldown:
            self.player.take_damage(14)
            for zombie in damage_cooldown:
                push_dir = zombie.position - self.player.position
                if push_dir.length_squared() > 0:
                    push_dir = push_dir.normalize()
                    zombie.position += push_dir * 14

    def render(self):
        self.screen.fill((25, 28, 34))

        if self.state == GameState.MENU:
            draw_menu(
                self.screen,
                self.width,
                self.height,
                self.menu_selection,
                self.player_name,
                self.leaderboard_lines,
            )
        elif self.state == GameState.NAME_INPUT:
            draw_name_input(self.screen, self.width, self.height, self.name_input)
        elif self.state == GameState.PLAYING:
            for projectile in self.projectiles:
                projectile.draw(self.screen)
            for zombie in self.zombies:
                zombie.draw(self.screen)
            aim_direction = pygame.Vector2(pygame.mouse.get_pos()) - self.player.position
            self.player.draw(self.screen)
            self.player.draw_barrel(self.screen, aim_direction)
            draw_hud(self.screen, self.kills, self.survival_time, self.player.health, self.player.max_health)
        elif self.state == GameState.GAME_OVER:
            for zombie in self.zombies:
                zombie.draw(self.screen)
            self.player.draw(self.screen)
            draw_game_over(self.screen, self.width, self.height, self.kills, self.survival_time)

        pygame.display.flip()

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
