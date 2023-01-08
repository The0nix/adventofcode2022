from collections.abc import Iterable

from solution import SolutionFromLines
from day2.figure import Figure, FigureType
from day2.game import Game


OPPONENT_TO_FIGURE_TYPE = {
    'A': FigureType.ROCK,
    'B': FigureType.PAPER,
    'C': FigureType.SCISSORS,
}
ME_TO_FIGURE_TYPE = {
    'X': FigureType.ROCK,
    'Y': FigureType.PAPER,
    'Z': FigureType.SCISSORS,
}


def game_from_line_part1(line: str) -> Game:
    opponent_str, me_str = line.strip().split()
    return Game(Figure(OPPONENT_TO_FIGURE_TYPE[opponent_str]), Figure(ME_TO_FIGURE_TYPE[me_str]))


FIGURE_TYPE_TO_HIGHER = {
    FigureType.ROCK: FigureType.PAPER,
    FigureType.PAPER: FigureType.SCISSORS,
    FigureType.SCISSORS: FigureType.ROCK,
}

FIGURE_TYPE_TO_LOWER = {
    FigureType.PAPER: FigureType.ROCK,
    FigureType.SCISSORS: FigureType.PAPER,
    FigureType.ROCK: FigureType.SCISSORS,
}


def game_from_line_part2(line: str) -> Game:
    opponent_str, me_str = line.strip().split()
    opponent_figure = Figure(OPPONENT_TO_FIGURE_TYPE[opponent_str])
    if me_str == 'X':  # Lose
        me_figure = Figure(FIGURE_TYPE_TO_LOWER[opponent_figure.type])
    elif me_str == 'Y':  # Draw
        me_figure = Figure(opponent_figure.type)
    elif me_str == 'Z':  # Win
        me_figure = Figure(FIGURE_TYPE_TO_HIGHER[opponent_figure.type])
    else:
        raise ValueError(f'Unknown input: {me_str}')
    return Game(opponent_figure, me_figure)


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        if self.part == 1:
            return sum(game_from_line_part1(line).score for line in lines)
        else:
            return sum(game_from_line_part2(line).score for line in lines)
