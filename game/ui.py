import pygame


def draw_menu(screen: pygame.Surface, width: int, height: int, selected_index: int):
    title_font = pygame.font.SysFont("arial", 56, bold=True)
    option_font = pygame.font.SysFont("arial", 36)

    title = title_font.render("Zombie Defense", True, (230, 230, 255))
    screen.blit(title, title.get_rect(center=(width // 2, height // 3)))

    options = ["Start", "Konec"]
    for i, text in enumerate(options):
        color = (255, 240, 90) if i == selected_index else (230, 230, 230)
        label = option_font.render(text, True, color)
        screen.blit(label, label.get_rect(center=(width // 2, height // 2 + i * 50)))


def draw_hud(screen: pygame.Surface, kills: int, survival_time: float, health: int, max_health: int):
    font = pygame.font.SysFont("consolas", 24)
    text = f"Zombie: {kills}   Cas: {survival_time:05.1f}s"
    label = font.render(text, True, (245, 245, 245))
    screen.blit(label, (20, 16))

    bar_x, bar_y = 20, 48
    bar_width, bar_height = 220, 18
    ratio = 0 if max_health == 0 else health / max_health
    pygame.draw.rect(screen, (80, 30, 30), (bar_x, bar_y, bar_width, bar_height), border_radius=6)
    pygame.draw.rect(screen, (220, 70, 70), (bar_x, bar_y, int(bar_width * ratio), bar_height), border_radius=6)
    pygame.draw.rect(screen, (230, 230, 230), (bar_x, bar_y, bar_width, bar_height), 2, border_radius=6)


def draw_game_over(screen: pygame.Surface, width: int, height: int, kills: int, survival_time: float):
    big_font = pygame.font.SysFont("arial", 54, bold=True)
    body_font = pygame.font.SysFont("arial", 30)

    title = big_font.render("GAME OVER", True, (255, 90, 90))
    stats = body_font.render(f"Skore: {kills} zombie | Cas: {survival_time:0.1f}s", True, (240, 240, 240))
    help_text = body_font.render("R = znovu, M = menu, ESC = konec", True, (190, 190, 190))

    screen.blit(title, title.get_rect(center=(width // 2, height // 2 - 70)))
    screen.blit(stats, stats.get_rect(center=(width // 2, height // 2 - 10)))
    screen.blit(help_text, help_text.get_rect(center=(width // 2, height // 2 + 40)))
