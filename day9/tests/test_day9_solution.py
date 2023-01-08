from pathlib import Path

from testing.solution_tester import SolutionTester
from day9.solution import DaySolution


def test_part1_1() -> None:
    solution_tester = SolutionTester(DaySolution(part=1))
    solution_tester.test(Path('day9/test_input.txt'), 13)


def test_part2_1() -> None:
    solution_tester = SolutionTester(DaySolution(part=2))
    solution_tester.test(Path('day9/test_input.txt'), 1)


def test_part2_2() -> None:
    solution_tester = SolutionTester(DaySolution(part=2))
    solution_tester.test(Path('day9/test_input2.txt'), 36)
