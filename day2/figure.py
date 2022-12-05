from __future__ import annotations
from enum import Enum


class FigureType(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Figure:
    FIGURE_TYPE_TO_SCORE = {
        FigureType.ROCK: 1,
        FigureType.PAPER: 2,
        FigureType.SCISSORS: 3,
    }

    def __init__(self, type: FigureType) -> None:
        self.type = type

    def __eq__(self, other: Figure) -> bool:
        return self.type == other.type

    def __lt__(self, other: Figure) -> bool:
        if (
            self.type == FigureType.ROCK and other.type == FigureType.PAPER or
            self.type == FigureType.PAPER and other.type == FigureType.SCISSORS or
            self.type == FigureType.SCISSORS and other.type == FigureType.ROCK
        ):
            return True
        return False

    @property
    def score(self) -> int:
        return self.FIGURE_TYPE_TO_SCORE[self.type]
