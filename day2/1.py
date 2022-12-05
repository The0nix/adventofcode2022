from pathlib import Path

import click

from figure import Figure, FigureType
from game import Game


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


def game_from_line(line: str) -> Game:
    opponent_str, me_str = line.strip().split()
    return Game(Figure(OPPONENT_TO_FIGURE_TYPE[opponent_str]), Figure(ME_TO_FIGURE_TYPE[me_str]))


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        result = sum(game_from_line(line).score for line in f)
    print(result)


if __name__ == '__main__':
    main()
