from collections.abc import Iterable

from solution import SolutionFromLines
from day4.interval import Interval


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        if self.part == 1:
            result = 0
            for line in lines:
                first_string, second_string = line.split(',')
                first = Interval.from_string(first_string)
                second = Interval.from_string(second_string)
                if first in second or second in first:
                    result += 1
            return result
        else:
            result = 0
            for line in lines:
                first_string, second_string = line.split(',')
                first = Interval.from_string(first_string)
                second = Interval.from_string(second_string)
                result += len(first & second) > 0
            return result
