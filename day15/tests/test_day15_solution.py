from pathlib import Path

from testing.solution_tester import SolutionTester
from day15.solution import DaySolution


def test_part1() -> None:
    solution_tester = SolutionTester(DaySolution(part=1, y=10))
    solution_tester.test(Path('day15/test_input.txt'), 26)


def test_part2() -> None:
    solution_tester = SolutionTester(DaySolution(part=2, interval_end=20))
    solution_tester.test(Path('day15/test_input.txt'), 56000011)
