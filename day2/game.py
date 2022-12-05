from __future__ import annotations

from figure import Figure


class Game:
    def __init__(self, opponent: Figure, me: Figure) -> None:
        self.opponent = opponent
        self.me = me

    @classmethod
    def from_line(cls, line: str) -> Game:
        opponent, me = line.strip().split()
        return cls(opponent, me)

    @property
    def score(self) -> int:
        score = self.me.score
        if self.me > self.opponent:
            score += 6
        elif self.me == self.opponent:
            score += 3
        return score
