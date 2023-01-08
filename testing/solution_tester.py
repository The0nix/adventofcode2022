from pathlib import Path
from typing import TypeVar, Generic

from solution import Solution

T = TypeVar('T')


class SolutionTester(Generic[T]):
    def __init__(self, solution: Solution[T]) -> None:
        self.solution = solution

    def test(self, input_file_path: Path, answer: T):
        assert self.solution.solve(input_file_path) == answer
