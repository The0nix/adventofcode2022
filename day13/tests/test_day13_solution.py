from pathlib import Path

from testing.solution_tester import SolutionTester
from day13.solution import DaySolution


def test_part1() -> None:
    solution_tester = SolutionTester(DaySolution(part=1))
    solution_tester.test(Path('day13') / 'inputs' / 'input_test.txt', 13)


def test_part2() -> None:
    solution_tester = SolutionTester(DaySolution(part=2))
    solution_tester.test(Path('day13') / 'inputs' / 'input_test.txt', 140)
