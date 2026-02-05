import pygame


def draw_menu(
    screen: pygame.Surface,
    width: int,
    height: int,
    selected_index: int,
    player_name: str,
    leaderboard_lines: list[str],
):
    title_font = pygame.font.SysFont("arial", 56, bold=True)
    option_font = pygame.font.SysFont("arial", 36)
    body_font = pygame.font.SysFont("consolas", 22)

    title = title_font.render("Zombie Defense", True, (230, 230, 255))
    screen.blit(title, title.get_rect(center=(width // 2, height // 4)))

    name_text = body_font.render(f"Hrac: {player_name or 'nezadano'}", True, (200, 220, 240))
    screen.blit(name_text, name_text.get_rect(center=(width // 2, height // 4 + 50)))

    options = ["Start", "Konec"]
    for i, text in enumerate(options):
        color = (255, 240, 90) if i == selected_index else (230, 230, 230)
        label = option_font.render(text, True, color)
        screen.blit(label, label.get_rect(center=(width // 2, height // 2 + i * 50)))

    score_title = body_font.render("Top vysledky (jmeno | skore | datum)", True, (220, 220, 220))
    screen.blit(score_title, (width // 2 - 260, height // 2 + 130))
    for index, line in enumerate(leaderboard_lines):
        label = body_font.render(f"{index + 1}. {line}", True, (190, 210, 220))
        screen.blit(label, (width // 2 - 260, height // 2 + 160 + index * 26))


def draw_name_input(screen: pygame.Surface, width: int, height: int, input_name: str):
    title_font = pygame.font.SysFont("arial", 46, bold=True)
    body_font = pygame.font.SysFont("arial", 28)

    title = title_font.render("Zadej jmeno hrace", True, (230, 230, 255))
    screen.blit(title, title.get_rect(center=(width // 2, height // 2 - 70)))

    entry = body_font.render(input_name or "_", True, (255, 240, 90))
    screen.blit(entry, entry.get_rect(center=(width // 2, height // 2 - 10)))

    hint = body_font.render("ENTER = pokracovat, ESC = zpet", True, (180, 180, 180))
    screen.blit(hint, hint.get_rect(center=(width // 2, height // 2 + 50)))


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
