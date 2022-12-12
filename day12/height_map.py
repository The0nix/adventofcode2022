from __future__ import annotations
import collections
from typing import Iterable, Optional, Union
from dataclasses import dataclass

Height = str

@dataclass(order=True, frozen=True)
class Position:
    x: int = 0
    y: int = 0

    def __add__(self, other: Union[Position, tuple[int, int]]) -> Position:
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        elif (isinstance(other, tuple) and len(other) == 2  # type: ignore
                and isinstance(other[0], int) and isinstance(other[1], int)):  # type: ignore
            return Position(self.x + other[0], self.y + other[1])
        else:
            return NotImplemented


class HeightMap:
    def __init__(self, lines: Iterable[str]) -> None:
        self._map: list[list[Height]] = []
        for x, line in enumerate(lines):
            self._map.append([])
            for y, char in enumerate(line):
                if char == 'S':
                    self._start = Position(x, y)
                    char = 'a'
                elif char == 'E':
                    self._end = Position(x, y)
                    char = 'z'
                self._map[-1].append(char)
        self._height = len(self._map)
        self._width = len(self._map[0])

    def _get_neighbours(self, position: Position, reverse: bool = False) -> list[Position]:
        result: list[Position] = []
        current_height = self._map[position.x][position.y]
        for shift in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbour_position = position + shift
            if neighbour_position.x < 0 or neighbour_position.x >= self._height \
                    or neighbour_position.y < 0 or neighbour_position.y >= self._width:
                continue
            neighbour_height = self._map[neighbour_position.x][neighbour_position.y]
            diff = ord(neighbour_height) - ord(current_height)
            if (not reverse and diff <= 1) or (reverse and diff >= -1):
                result.append(neighbour_position)
        return result

    def _get_shortest_path_length(
        self, start: Position, end: Union[Position, Height], reverse: bool = False
    ) -> Optional[int]:
        layer = 0
        used: set[Position] = set([start])
        queue: collections.deque[Optional[Position]] = collections.deque([start, None])
        while queue:
            current_position = queue.popleft()
            if current_position is None:
                if queue:
                    queue.append(None)  # Indicates the end of layer
                layer += 1
                continue
            if isinstance(end, Position) and current_position == end:
                return layer
            if isinstance(end, Height) and self._map[current_position.x][current_position.y] == end:
                return layer
            for neighbour in self._get_neighbours(current_position, reverse=reverse):
                if neighbour not in used:
                    queue.append(neighbour)
                    used.add(neighbour)
        return None

    def find_path_to_end_length(self) -> Optional[int]:
        return self._get_shortest_path_length(self._start, self._end)

    def find_hiking_trail_length(self) -> Optional[int]:
        # from tqdm.auto import tqdm
        # results: list[int] = []
        # for x in tqdm(range(len(self._map))):
        #     for y in tqdm(range(len(self._map[0])), leave=False):
        #         if self._map[x][y] == 'a':
        #             result = self._get_shortest_path_length(Position(x, y), self._end)
        #             if result is not None:
        #                 results.append(result)
        # return min(results)
        return self._get_shortest_path_length(self._end, 'a', reverse=True)
