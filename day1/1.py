from pathlib import Path

import click

from elf import Elf


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    max_calories = -1
    with open(input) as f:
        current_elf = Elf()
        for line in f:
            if line.strip():
                current_elf.add_item(int(line))
            else:
                if current_elf.total_calories > max_calories:
                    max_calories = current_elf.total_calories
                current_elf = Elf()
    print(max_calories)


if __name__ == '__main__':
    main()
