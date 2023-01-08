from collections.abc import Iterable

from solution import SolutionFromLines
from day14.cave import Cave


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        has_floor = False if self.part == 1 else True

        cave = Cave(lines, has_floor=has_floor)
        cave.print_map()
        result = cave.determine_sand_capacity()
        return result
