import copy
from collections.abc import Iterable

from day11.monkey import Monkey

MonkeyLevel = int


class KeepAway:
    def __init__(self, monkeys: Iterable[Monkey]) -> None:
        self._monkeys: list[Monkey] = list(monkeys)
        self._monkey_levels: list[MonkeyLevel] = [0 for _ in self._monkeys]

    def do_round(self):
        for current_monkey_id, monkey in enumerate(self._monkeys):
            for item, target_monkey_id in monkey.do_turn():
                self._monkeys[target_monkey_id].add_item(item)
                self._monkey_levels[current_monkey_id] += 1

    @property
    def monkey_levels(self) -> list[MonkeyLevel]:
        return copy.deepcopy(self._monkey_levels)
