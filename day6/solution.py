import itertools
from pathlib import Path

from solution import Solution, SolutionNotFoundError
from day6.unique_counting_limited_queue import UniqueCountingLimitedQueue


class DaySolution(Solution[int]):
    def solve(self, input_file_path: Path) -> int:
        with open(input_file_path) as f:
            max_n = 4 if self.part == 1 else 14
            uclq: UniqueCountingLimitedQueue[str] = UniqueCountingLimitedQueue(max_n)
            for i in itertools.count(1):
                symbol = f.read(1)
                if symbol == '\n':
                    break
                uclq.append(symbol)
                if uclq.n_unique == max_n:
                    return i
            raise SolutionNotFoundError
