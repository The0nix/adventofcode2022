from pathlib import Path

import click

from crt import CRT


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    crt = CRT()
    with open(input) as f:
        crt.execute_commands((line.strip() for line in f))
        crt.draw_image()


if __name__ == '__main__':
    main()
