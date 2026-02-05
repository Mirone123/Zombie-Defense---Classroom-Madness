import random
import pygame


class Zombie:
    def __init__(self, x: float, y: float, speed: float = 90, radius: int = 16):
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.radius = radius
        self.damage = 12
        self.color = (70, 200, 110)

    @staticmethod
    def spawn_at_screen_edge(world_rect: pygame.Rect) -> "Zombie":
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            x = random.uniform(world_rect.left, world_rect.right)
            y = world_rect.top - 20
        elif side == "bottom":
            x = random.uniform(world_rect.left, world_rect.right)
            y = world_rect.bottom + 20
        elif side == "left":
            x = world_rect.left - 20
            y = random.uniform(world_rect.top, world_rect.bottom)
        else:
            x = world_rect.right + 20
            y = random.uniform(world_rect.top, world_rect.bottom)

        speed = random.uniform(80, 130)
        return Zombie(x, y, speed=speed)

    def update(self, dt: float, player_position: pygame.Vector2):
        direction = player_position - self.position
        if direction.length_squared() > 0:
            direction = direction.normalize()
        self.position += direction * self.speed * dt

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
