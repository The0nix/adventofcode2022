from pathlib import Path

from testing.solution_tester import SolutionTester
from day7.solution import DaySolution


def test_part1() -> None:
    solution_tester = SolutionTester(DaySolution(part=1))
    solution_tester.test(Path('day7') / 'inputs' / 'input_test.txt', 95437)


def test_part2() -> None:
    solution_tester = SolutionTester(DaySolution(part=2))
    solution_tester.test(Path('day7') / 'inputs' / 'input_test.txt', 24933642)
