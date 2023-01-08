from collections.abc import Iterable

from solution import SolutionFromLines
from day12.height_map import HeightMap


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        height_map = HeightMap(lines)
        if self.part == 1:
            result = height_map.find_path_to_end_length()
        else:
            result = height_map.find_hiking_trail_length()
        assert result is not None, 'No solution'
        return result
