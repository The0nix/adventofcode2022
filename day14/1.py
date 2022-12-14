from pathlib import Path

import click

from cave import Cave


@click.command()
@click.argument('input', type=Path)
@click.option('--animate', is_flag=True)
@click.option('--animation-delay', type=float, default=0.1)
def main(input: Path, animate: bool, animation_delay: float) -> None:
    with open(input) as f:
        lines = (line.strip() for line in f)
        cave = Cave(lines)
        cave.print_map()
        result = cave.determine_sand_capacity(animate=animate, animation_delay=animation_delay)
        print(result)


if __name__ == '__main__':
    main()
