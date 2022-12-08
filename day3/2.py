from pathlib import Path
from typing import Iterable, Generator, TypeVar

import click

from rucksack import Rucksack

T = TypeVar('T')


def read_triplets(iterable: Iterable[T]) -> Generator[tuple[T, T, T], None, None]:
    triplet: list[T] = []
    for obj in iterable:
        triplet.append(obj)
        if len(triplet) == 3:
            yield tuple(triplet)
            triplet = []


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    result = 0
    with open(input) as f:
        result = sum(
            Rucksack.get_item_priority(
                (Rucksack(r1).whole & Rucksack(r2).whole & Rucksack(r3).whole).pop()
             ) for r1, r2, r3 in read_triplets(line.strip() for line in f)
        )
    print(result)


if __name__ == '__main__':
    main()
