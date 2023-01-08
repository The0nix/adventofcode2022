import math
import itertools
import heapq
from collections.abc import Iterable

from tqdm.auto import tqdm

from solution import SolutionFromLines
from day11.monkey import Monkey
from day11.keep_away import KeepAway


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        rounds = 20 if self.part == 1 else 10000
        decrease_worry_level = True if self.part == 1 else False

        monkeys_list: list[Monkey] = []
        lines_iter = iter(lines)
        while True:
            next(lines_iter)
            monkeys_list.append(Monkey(list(itertools.islice(lines_iter, 0, 5)), decrease_worry_level))
            try:
                next(lines_iter)
            except StopIteration:
                break
        modulus = math.lcm(*(monkey.test.divisor for monkey in monkeys_list))
        for monkey in monkeys_list:
            monkey.modulus = modulus
        keep_away = KeepAway(monkeys_list)
        for _ in tqdm(range(rounds)):
            keep_away.do_round()
        monkey_levels = keep_away.monkey_levels
        two_largest = heapq.nlargest(2, monkey_levels)
        return two_largest[0] * two_largest[1]
