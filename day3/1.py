from pathlib import Path

import click

from rucksack import Rucksack


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        result = sum(Rucksack.get_item_priority(Rucksack(line.strip()).get_shared_item()) for line in f)
    print(result)


if __name__ == '__main__':
    main()
