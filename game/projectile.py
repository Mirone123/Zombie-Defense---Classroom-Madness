import pygame


class Projectile:
    def __init__(self, start_pos: pygame.Vector2, direction: pygame.Vector2, speed: float = 520, radius: int = 4):
        self.position = pygame.Vector2(start_pos)
        if direction.length_squared() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(1, 0)
        self.speed = speed
        self.radius = radius
        self.color = (255, 220, 80)

    def update(self, dt: float):
        self.position += self.direction * self.speed * dt

    def is_out_of_bounds(self, world_rect: pygame.Rect) -> bool:
        margin = 50
        expanded = world_rect.inflate(margin * 2, margin * 2)
        return not expanded.collidepoint(self.position.x, self.position.y)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
