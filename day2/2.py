from pathlib import Path

import click

from figure import Figure, FigureType
from game import Game


OPPONENT_TO_FIGURE_TYPE = {
    'A': FigureType.ROCK,
    'B': FigureType.PAPER,
    'C': FigureType.SCISSORS,
}

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


def game_from_line(line: str) -> Game:
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


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        result = sum(game_from_line(line).score for line in f)
    print(result)


if __name__ == '__main__':
    main()
