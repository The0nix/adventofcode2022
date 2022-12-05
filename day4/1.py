from pathlib import Path

import click

from interval import Interval


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    result = 0
    with open(input) as f:
        for line in f:
            first_string, second_string = line.strip().split(',')
            first = Interval.from_string(first_string)
            second = Interval.from_string(second_string)
            if first in second or second in first:
                result += 1
    print(result)


if __name__ == '__main__':
    main()
