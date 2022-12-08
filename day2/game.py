from __future__ import annotations

from figure import Figure


class Game:
    def __init__(self, opponent: Figure, me: Figure) -> None:
        self.opponent = opponent
        self.me = me

    @property
    def score(self) -> int:
        score = self.me.score
        if self.me > self.opponent:
            score += 6
        elif self.me == self.opponent:
            score += 3
        return score
