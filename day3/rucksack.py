from __future__ import annotations
import string

PRIORITY_MAP = {item: index for index, item in enumerate(string.ascii_letters, 1)}


class Rucksack:
    def __init__(self, string: str) -> None:
        self.whole = set(string)
        self.compartment1 = set(string[:len(string) // 2])
        self.compartment2 = set(string[len(string) // 2:])

    def get_shared_item(self) -> str:
        return (self.compartment1 & self.compartment2).pop()

    @staticmethod
    def get_item_priority(item: str) -> int:
        return PRIORITY_MAP[item]
