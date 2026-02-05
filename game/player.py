import pygame


class Player:
    def __init__(self, x: float, y: float, speed: float = 280, radius: int = 18):
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.radius = radius
        self.max_health = 100
        self.health = self.max_health
        self.color = (70, 160, 255)

    def reset(self, x: float, y: float):
        self.position.update(x, y)
        self.health = self.max_health

    def update(self, dt: float, input_vector: pygame.Vector2, world_rect: pygame.Rect):
        if input_vector.length_squared() > 0:
            input_vector = input_vector.normalize()
        self.position += input_vector * self.speed * dt

        self.position.x = max(world_rect.left + self.radius, min(self.position.x, world_rect.right - self.radius))
        self.position.y = max(world_rect.top + self.radius, min(self.position.y, world_rect.bottom - self.radius))

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def draw_barrel(self, screen: pygame.Surface, aim_direction: pygame.Vector2):
        if aim_direction.length_squared() == 0:
            aim_direction = pygame.Vector2(1, 0)
        else:
            aim_direction = aim_direction.normalize()
        end_pos = self.position + aim_direction * (self.radius + 10)
        pygame.draw.line(screen, (220, 240, 255), self.position, end_pos, 4)
