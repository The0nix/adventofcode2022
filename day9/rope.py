from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


@dataclass(eq=True, frozen=True)
class Position:
    x: int = 0
    y: int = 0

    def __add__(self, other: Position | tuple[int, int]) -> Position:
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):  # type: ignore
            return Position(self.x + other[0], self.y + other[1])
        else:
            return NotImplemented
        
    def __sub__(self, other: Position | tuple[int, int]) -> Position:
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        elif isinstance(other, tuple):  # type: ignore
            return Position(self.x - other[0], self.y - other[1])
        else:
            return NotImplemented

    def __neg__(self) -> Position:
        return Position(-self.x, -self.y)
    

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Rope:
    def __init__(self, tail_length: int = 1) -> None:
        self._all_positions = [Position() for _ in range(tail_length + 1)]

    def move_head(self, direction: Direction) -> Position:
        """Moves head and returns new tail position"""
        if direction == Direction.UP:
            self._all_positions[0] += (0, 1)
        elif direction == Direction.DOWN:
            self._all_positions[0] += (0, -1)
        elif direction == Direction.LEFT:
            self._all_positions[0] += (-1, 0)
        elif direction == Direction.RIGHT:
            self._all_positions[0] += (1, 0)
        else:
            raise ValueError(f'Unknown direction: {direction}')
        return self._update_tail()

    def _update_tail(self) -> Position:
        for i in range(1, len(self._all_positions)):
            self._all_positions[i] = self._follow_segment(self._all_positions[i - 1], self._all_positions[i])
        return self._all_positions[-1]

    def _are_adjacent(self, first: Position, second: Position) -> bool:
        difference = second - first
        if abs(difference.x) > 1 or abs(difference.y) > 1:
            return False
        return True

    def _follow_segment(self, first: Position, second: Position) -> Position:
        if self._are_adjacent(first, second):
            return second

        if second.x == first.x:
            if second.y < first.y:
                second += (0, 1)
            else:
                second += (0, -1)
        elif second.y == first.y:
            if second.x < first.x:
                second += (1, 0)
            else:
                second += (-1, 0)
        elif second.x < first.x and second.y < first.y:
            second += (1, 1)
        elif second.x < first.x and second.y > first.y:
            second += (1, -1)
        elif second.x > first.x and second.y < first.y:
            second += (-1, 1)
        elif second.x > first.x and second.y > first.y:
            second += (-1, -1)

        return second
