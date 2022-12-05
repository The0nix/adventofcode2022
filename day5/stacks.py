import collections
from typing import Iterable


class Stacks:
    def __init__(self) -> None:
        self.stacks = collections.defaultdict(list)

    @classmethod
    def from_lines(cls, f: Iterable):
        object = cls()
        for line in f:
            if line[1] == '1':
                break
            for i in range(len(line) // 4):
                letter = line[i * 4 + 1:i * 4 + 2]
                if letter != ' ':
                    object.add_box(i + 1, letter)
        object.reverse()
        return object

    def add_box(self, index: int, letter: str) -> None:
        self.stacks[index].append(letter)

    def reverse(self) -> None:
        """Reverse boxes in each stack"""
        for stack in self.stacks.values():
            stack.reverse()

    def move(self, number: int, from_index: int, to_index: int, reverse=True) -> None:
        boxes_to_move = self.stacks[from_index][-number:]
        del self.stacks[from_index][-number:]
        if reverse:
            boxes_to_move.reverse()
        self.stacks[to_index].extend(boxes_to_move)

    def get_tops(self):
        return [stack[-1] for index, stack in sorted(self.stacks.items(), key=lambda item: item[0])]

    def print_drawing(self):
        height = max(len(s) for s in self.stacks.values())
        sorted_stacks = sorted(self.stacks.items(), key=lambda item: item[0])
        for cur_height in range(height, -1, -1):
            for _, stack in sorted_stacks:
                if len(stack) > cur_height:
                    print(f'[{stack[cur_height]}]', end=' ')
                else:
                    print('   ', end=' ')
            print()
        for number, _ in sorted_stacks:
            print(f' {number} ', end=' ')
        print()
