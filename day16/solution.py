from collections.abc import Iterable

from solution import SolutionFromLines
from day16.pipe_network import PipeNetwork


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        pipe_network = PipeNetwork(lines)
        if self.part == 1:
            result = pipe_network.get_best_pressure()
        else:
            result = pipe_network.get_best_pressure_with_elephant()
        return result
