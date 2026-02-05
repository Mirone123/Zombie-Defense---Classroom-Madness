import random
import sys
import types


class _FakeVector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, _FakeVector2) and self.x == other.x and self.y == other.y


fake_pygame = types.SimpleNamespace(Vector2=_FakeVector2, Rect=object, Surface=object)
sys.modules.setdefault("pygame", fake_pygame)

from game.enemy import Zombie


class _WorldRect:
    def __init__(self, left: float, top: float, width: float, height: float):
        self.left = left
        self.top = top
        self.right = left + width
        self.bottom = top + height


def test_spawn_at_edge_is_deterministic_with_seed():
    world_rect = _WorldRect(0, 0, 1000, 700)

    random.seed(12345)
    first_spawn = Zombie.spawn_at_screen_edge(world_rect)

    random.seed(12345)
    second_spawn = Zombie.spawn_at_screen_edge(world_rect)

    assert first_spawn.position == second_spawn.position
    assert first_spawn.speed == second_spawn.speed

    x = first_spawn.position.x
    y = first_spawn.position.y

    assert (
        y == world_rect.top - 20
        or y == world_rect.bottom + 20
        or x == world_rect.left - 20
        or x == world_rect.right + 20
    )
    assert 80 <= first_spawn.speed <= 130
