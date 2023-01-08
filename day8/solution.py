from collections.abc import Iterable
from enum import Enum

from solution import SolutionFromLines
from day8.forest import Forest


class STATE(Enum):
    INPUT_COMMAND = 1
    READ_LS_OUTPUT = 2


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        forest = Forest.from_lines(lines)
        if self.part == 1:
            forest.calculate_visibility()
            result = forest.count_visible()
        else:
            forest.calculate_scenic_scores()
            result = forest.get_maximum_scenic_score()
        print(forest)
        return result

