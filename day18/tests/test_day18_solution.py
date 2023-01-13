from pathlib import Path

from testing.solution_tester import SolutionTester
from day18.solution import DaySolution


def test_part1() -> None:
    solution_tester = SolutionTester(DaySolution(part=1))
    solution_tester.test(Path('day18') / 'inputs' / 'input_test.txt', 64)


def test_part2() -> None:
    solution_tester = SolutionTester(DaySolution(part=2))
    solution_tester.test(Path('day18') / 'inputs' / 'input_test.txt', 58)
