from __future__ import annotations
from typing import Union
from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Position:
    x: int = 0  # Horizontal left to right
    y: int = 0  # Vertical bottom to top

    def __add__(self, other: Union[Position, tuple[int, int]]) -> Position:
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        elif (isinstance(other, tuple) and len(other) == 2  # type: ignore
                and isinstance(other[0], int) and isinstance(other[1], int)):  # type: ignore
            return Position(self.x + other[0], self.y + other[1])
        else:
            return NotImplemented
