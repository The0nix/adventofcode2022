import re
import itertools
import math
from dataclasses import dataclass
from typing import Iterable, Optional

Items = list[int]
MonkeyID = int
WorryLevel = int


def _remove_prefix(string: str, prefix: str, raise_error: bool = True):
    if string.startswith(prefix):
        return string[len(prefix):]
    elif not raise_error:
        return string
    else:
        raise ValueError(f'String {string} doesn\'t start with prefix {prefix}')


@dataclass
class Item:
    def __init__(self, worry_level: WorryLevel):
        self.worry_level = worry_level


class Operation:
    def __init__(self, string: str) -> None:
        string = _remove_prefix(string, 'Operation: new = ')
        match = re.match(r'^(?P<first>.*?) (?P<op>.*?) (?P<second>.*?)$', string)
        assert match is not None, f'Incorrect operation format: {string}'
        self._first = 'old' if match['first'] == 'old' else WorryLevel(match['first'])
        self._second = 'old' if match['second'] == 'old' else WorryLevel(match['second'])
        assert match['op'] in ['+', '*']
        self._op = match['op']

    def __call__(self, value: WorryLevel) -> WorryLevel:
        first = value if self._first == 'old' else self._first
        second = value if self._second == 'old' else self._second
        if self._op == '+':
            return first + second  # type: ignore
        elif self._op == '*':
            return first * second  # type: ignore
        else:
            raise ValueError


class Test:
    def __init__(self, lines: Iterable[str]) -> None:
        iterator = iter(lines)
        self._divisor = int(_remove_prefix(next(iterator), 'Test: divisible by '))
        self._true_monkey_id = MonkeyID(_remove_prefix(next(iterator), 'If true: throw to monkey '))
        self._false_monkey_id = MonkeyID(_remove_prefix(next(iterator), 'If false: throw to monkey '))

    @property
    def divisor(self):
        return self._divisor

    def __call__(self, value: WorryLevel) -> MonkeyID:
        if value % self._divisor == 0:
            return self._true_monkey_id
        else:
            return self._false_monkey_id


class Monkey:
    def __init__(self, lines: Iterable[str], decrease_worry_level: bool = True, modulus: Optional[int] = None):
        self._decrease_worry_level = decrease_worry_level
        self._modulus = modulus

        iterator = iter(lines)
        items_string = _remove_prefix(next(iterator), 'Starting items: ')
        self._items: list[Item] = [Item(WorryLevel(item)) for item in items_string.split(', ')]
        self._operation = Operation(next(iterator))
        self._test = Test(itertools.islice(iterator, 0, 3))

    def set_modulus(self, value: Optional[int]):
        self._modulus = value

    @property
    def items(self):
        return self._items

    @property
    def operation(self):
        return self._operation

    @property
    def test(self):
        return self._test

    @property
    def modulus(self):
        return self._modulus
    
    @modulus.setter
    def modulus(self, value: Optional[int] = None):
        self._modulus = value

    def do_turn(self) -> list[tuple[Item, MonkeyID]]:
        """Performs one turn of a monkey. Returns list of pairs: [(item_to_throw, target_monkey_id), ...]"""
        result: list[tuple[Item, MonkeyID]] = []
        for item in self._items:
            item.worry_level = self._operation(item.worry_level)
            if self._decrease_worry_level:
                item.worry_level = int(math.floor(item.worry_level / 3))
            if self._modulus is not None:
                item.worry_level = item.worry_level % self._modulus
            target_monkey_id = self._test(item.worry_level)
            result.append((item, target_monkey_id))
        self._items = []
        return result

    def add_item(self, item: Item) -> None:
        self._items.append(item)
