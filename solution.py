from pathlib import Path

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TypeVar, Generic

T = TypeVar('T')


class SolutionNotFoundError(Exception):
    pass


class Solution(ABC, Generic[T]):
    def __init__(self, part: int):
        assert part in [1, 2]
        self.part = part

    @abstractmethod
    def solve(self, input_file_path: Path) -> T:
        pass


class SolutionFromLines(Solution[T]):
    def solve(self, input_file_path: Path) -> T:
        with open(input_file_path) as f:
            lines = (line.strip() for line in f)
            return self.solve_impl(lines)

    @abstractmethod
    def solve_impl(self, lines: Iterable[str]) -> T:
        pass
