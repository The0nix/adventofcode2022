from pathlib import Path

import click

from elf import Elf


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    max_calories = [-1, -1, -1]
    with open(input) as f:
        current_elf = Elf()
        for line in f:
            if line.strip():
                current_elf.add_item(int(line))
            else:
                for i in range(len(max_calories)):
                    if current_elf.total_calories > max_calories[i]:
                        max_calories[i] = current_elf.total_calories
                        break
                current_elf = Elf()
    print(sum(max_calories))


if __name__ == '__main__':
    main()
