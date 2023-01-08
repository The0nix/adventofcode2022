from pathlib import Path

from testing.solution_tester import SolutionTester
from day16.solution import DaySolution


def test_part1() -> None:
    solution_tester = SolutionTester(DaySolution(part=1))
    solution_tester.test(Path('day16') / 'inputs' / 'input_test.txt', 1651)


def test_part2() -> None:
    solution_tester = SolutionTester(DaySolution(part=2))
    solution_tester.test(Path('day16') / 'inputs' / 'input_test.txt', 1707)
