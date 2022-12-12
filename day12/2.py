from pathlib import Path

import click

from height_map import HeightMap


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        height_map = HeightMap(line.strip() for line in f)
        result = height_map.find_hiking_trail_length()
        print(result)


if __name__ == '__main__':
    main()
