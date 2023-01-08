from typing import TypeVar
from collections.abc import Iterable, Generator

from solution import SolutionFromLines
from day3.rucksack import Rucksack


T = TypeVar('T')


def read_triplets(iterable: Iterable[T]) -> Generator[tuple[T, T, T], None, None]:
    triplet: list[T] = []
    for obj in iterable:
        triplet.append(obj)
        if len(triplet) == 3:
            yield tuple(triplet)
            triplet = []


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        if self.part == 1:
            return sum(Rucksack.get_item_priority(Rucksack(line.strip()).get_shared_item()) for line in lines)
        else:
            return sum(
                Rucksack.get_item_priority(
                    (Rucksack(r1).whole & Rucksack(r2).whole & Rucksack(r3).whole).pop()
                ) for r1, r2, r3 in read_triplets(line for line in lines)
            )
