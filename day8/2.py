from pathlib import Path

import click

from forest import Forest


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        forest = Forest.from_lines(line.strip() for line in f)
        forest.calculate_scenic_scores()
        print(forest)
        result = forest.get_maximum_scenic_score()
        print(result)


if __name__ == '__main__':
    main()
