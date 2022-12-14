from __future__ import annotations
import json
from typing import Union

PacketContents = Union[int, list['PacketContents']]


class Packet:
    def __init__(self, line: str) -> None:
        self._contents: PacketContents = json.loads(line)

    def compare(self, other: Packet) -> int:
        return self._compare_contents(self._contents, other._contents)

    def _compare_contents(self, left: PacketContents, right: PacketContents) -> int:
        if isinstance(left, int) and isinstance(right, int):
            return left - right
        elif isinstance(left, list) and isinstance(right, list):
            for ll, rr in zip(left, right):
                if (result := self._compare_contents(ll, rr)) != 0:
                    return result
            return len(left) - len(right)
        else:
            if isinstance(left, int):
                return self._compare_contents([left], right)
            else:
                return self._compare_contents(left, [right])

    def __lt__(self, other: Packet):
        if not isinstance(other, Packet):  # type: ignore
            return NotImplemented
        return self.compare(other) < 0

    def __gt__(self, other: object):
        if not isinstance(other, Packet):  # type: ignore
            return NotImplemented
        return self.compare(other) > 0
    
    def __eq__(self, other: object):
        if not isinstance(other, Packet):
            return NotImplemented
        return self.compare(other) == 0
