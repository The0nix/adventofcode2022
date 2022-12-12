import math
import itertools
import heapq
from pathlib import Path

from tqdm.auto import tqdm

import click
from monkey import Monkey
from keep_away import KeepAway


@click.command()
@click.argument('input', type=Path)
@click.option('--rounds', type=int, default=10000)
def main(input: Path, rounds: int) -> None:
    monkeys_list: list[Monkey] = []
    with open(input) as f:
        while True:
            stripped_lines = (line.strip() for line in f)
            next(stripped_lines)
            monkeys_list.append(Monkey(list(itertools.islice(stripped_lines, 0, 5)), False))
            try:
                next(stripped_lines)
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
    print(two_largest[0] * two_largest[1])


if __name__ == '__main__':
    main()
