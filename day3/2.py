from pathlib import Path
from typing import Iterable

import click

from rucksack import Rucksack


def read_triplets(f: Iterable):
    triplet = []
    for line in f:
        triplet.append(line.strip())
        if len(triplet) == 3:
            yield triplet
            triplet = []


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    result = 0
    with open(input) as f:
        result = sum(
            Rucksack.get_item_priority(
                (Rucksack(r1).whole & Rucksack(r2).whole & Rucksack(r3).whole).pop()
             ) for r1, r2, r3 in read_triplets(f)
        )
    print(result)


if __name__ == '__main__':
    main()
