from __future__ import annotations
from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Position:
    x: int = 0  # Horizontal left to right
    y: int = 0  # Vertical top to bottom
