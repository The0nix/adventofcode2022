from __future__ import annotations
import re
import time
import copy
from collections.abc import Iterable, Generator
from typing import Union
from dataclasses import dataclass
from enum import Enum


@dataclass(order=True, frozen=True)
class Position:
    x: int = 0  # Horizontal left to right
    y: int = 0  # Vertical top to bottom

    def __add__(self, other: Union[Position, tuple[int, int]]) -> Position:
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        elif (isinstance(other, tuple) and len(other) == 2  # type: ignore
                and isinstance(other[0], int) and isinstance(other[1], int)):  # type: ignore
            return Position(self.x + other[0], self.y + other[1])
        else:
            return NotImplemented


class CellType(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2


class Cave:
    POS_RE = re.compile(r'(?P<x>\d+),(?P<y>\d+)')
    PARTICLE_MAPPING = {
        CellType.AIR: '.',
        CellType.ROCK: '#',
        CellType.SAND: 'o',
    }

    def __init__(self, lines: Iterable[str], has_floor: bool = False) -> None:
        self._has_floor = has_floor
        self._map: dict[Position, CellType] = {}
        for line in lines:
            positions_list = [
                Position(**{k: int(v) for k, v in match.groupdict().items()}) 
                for match in self.POS_RE.finditer(line)
            ]
            for pos_from, pos_to in zip(positions_list[:-1], positions_list[1:]):
                for pos in self._make_trail(pos_from, pos_to):
                    self._map[pos] = CellType.ROCK

        self._max_x = max(pos.x for pos in self._map)
        self._min_x = min(pos.x for pos in self._map)
        self._max_y = max(pos.y for pos in self._map)
        self._min_y = min(pos.y for pos in self._map)

    @staticmethod
    def _make_trail(pos_from: Position, pos_to: Position) -> Generator[Position, None, None]:
        assert pos_from.x == pos_to.x or pos_from.y == pos_to.y, 'Can only make straight trails'
        if pos_from.x == pos_to.x:
            if pos_from.y > pos_to.y:
                pos_from, pos_to = pos_to, pos_from
            return (Position(pos_from.x, y) for y in range(pos_from.y, pos_to.y + 1))
        else:
            if pos_from.x > pos_to.x:
                pos_from, pos_to = pos_to, pos_from
            return (Position(x, pos_from.y) for x in range(pos_from.x, pos_to.x + 1))

    def determine_sand_capacity(
        self, sand_start: Position = Position(500, 0), animate: bool = False, animation_delay: float = 0.1
    ) -> int:
        map = copy.deepcopy(self._map)
        grains_count = 0
        while True:  # Grains spawn iterations
            if animate:
                print('>', grains_count)
                time.sleep(animation_delay)
                self._print_map(map)
            else:
                print(f'\r{grains_count}',end='')
            grain_position = copy.copy(sand_start)
            while True:  # Current grain fall iterations
                if not self._has_floor and grain_position.y > self._max_y:
                    self._print_map(map)
                    return grains_count
                if sand_start in map:
                    self._print_map(map)
                    return grains_count
                for shift in [(0, 1), (-1, 1), (1, 1)]:
                    if grain_position + shift not in map and not self._in_floor(grain_position + shift):
                        grain_position += shift
                        break
                else:
                    grains_count += 1
                    map[grain_position] = CellType.SAND
                    break

    def _in_floor(self, position: Position):
        if not self._has_floor:
            return False
        return position.y >= self._max_y + 2

    def _print_map(self, map: dict[Position, CellType]):
        max_x = max(pos.x for pos in map)
        min_x = min(pos.x for pos in map)
        max_y = max(pos.y for pos in map)
        min_y = min(pos.y for pos in map)

        for y in range(min_y, max_y + 1):
            for pos in self._make_trail(Position(min_x, y), Position(max_x, y)):
                print(self.PARTICLE_MAPPING[map.get(pos, CellType.AIR)], end='')
            print()

    def print_map(self):
        self._print_map(self._map)
