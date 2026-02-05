"""Player entity for top-down zombie defense gameplay."""

import pygame


class Player:
    """Represents the controllable player circle and its combat stats."""

    def __init__(self, x: float, y: float, speed: float = 280, radius: int = 18):
        # Current position in world coordinates.
        self.position = pygame.Vector2(x, y)
        # Movement speed in pixels per second.
        self.speed = speed
        # Collision radius.
        self.radius = radius
        # Health pool configuration.
        self.max_health = 100
        self.health = self.max_health
        self.color = (70, 160, 255)

    def reset(self, x: float, y: float):
        """Reset position and health before a new run."""
        self.position.update(x, y)
        self.health = self.max_health

    def update(self, dt: float, input_vector: pygame.Vector2, world_rect: pygame.Rect):
        """Move the player using normalized input and clamp to world bounds."""
        if input_vector.length_squared() > 0:
            input_vector = input_vector.normalize()
        self.position += input_vector * self.speed * dt

        self.position.x = max(world_rect.left + self.radius, min(self.position.x, world_rect.right - self.radius))
        self.position.y = max(world_rect.top + self.radius, min(self.position.y, world_rect.bottom - self.radius))

    def take_damage(self, amount: int):
        """Reduce health but never below zero."""
        self.health = max(0, self.health - amount)

    @property
    def is_alive(self) -> bool:
        """Whether the player is still alive."""
        return self.health > 0

    def draw(self, screen: pygame.Surface):
        """Render the player's body."""
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def draw_barrel(self, screen: pygame.Surface, aim_direction: pygame.Vector2):
        """Render a simple weapon barrel aimed towards current cursor direction."""
        if aim_direction.length_squared() == 0:
            aim_direction = pygame.Vector2(1, 0)
        else:
            aim_direction = aim_direction.normalize()
        end_pos = self.position + aim_direction * (self.radius + 10)
        pygame.draw.line(screen, (220, 240, 255), self.position, end_pos, 4)
