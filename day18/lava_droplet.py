from __future__ import annotations
import itertools
from collections.abc import Iterable
from collections import Counter, deque
from dataclasses import dataclass

from day18.cube import Cube, CubeSide


@dataclass(frozen=True)
class LavaDropletLimits:
    x: tuple[int, int]
    y: tuple[int, int]
    z: tuple[int, int]

    @classmethod
    def from_cubes(cls, cubes: Iterable[Cube]) -> LavaDropletLimits:
        x = [float('inf'), float('-inf')]
        y = [float('inf'), float('-inf')]
        z = [float('inf'), float('-inf')]
        for cube in cubes:
            x[0] = min(cube.x, x[0])
            x[1] = max(cube.x, x[1])
            y[0] = min(cube.y, y[0])
            y[1] = max(cube.y, y[1])
            z[0] = min(cube.z, z[0])
            z[1] = max(cube.z, z[1])
        for var in itertools.chain(x, y, z):
            assert isinstance(var, int)
        return cls(tuple(x), tuple(y), tuple(z))  # type: ignore



class LavaDroplet:
    def __init__(self, cubes: Iterable[Cube]) -> None:
        self.cubes = list(cubes)
        self.limits = LavaDropletLimits.from_cubes(self.cubes)

    @property
    def n_cubes(self) -> int:
        return len(self.cubes)

    def calculate_surface_area(self) -> int:
        cube_sides_counter: Counter[CubeSide] = Counter(
            itertools.chain.from_iterable(cube.sides for cube in self.cubes)
        )
        return sum(1 for value in cube_sides_counter.values() if value == 1)

    def calculate_outer_surface_area(self) -> int:
        outer_sides_set: set[CubeSide] = set()
        droplet_cubes_set = set(self.cubes)

        initial_space = Cube(self.limits.x[0] - 1, self.limits.y[0] - 1, self.limits.z[0] - 1)
        used_spaces = set([initial_space])
        spaces_stack = deque([initial_space])

        while spaces_stack:
            current_space = spaces_stack.pop()
            for neighbour_space in self._get_neighbour_spaces(current_space):
                if neighbour_space in droplet_cubes_set:
                    outer_sides_set.add(current_space.get_common_side(neighbour_space))
                elif neighbour_space not in used_spaces:
                    used_spaces.add(neighbour_space)
                    spaces_stack.append(neighbour_space)
        return len(outer_sides_set)

    def _get_neighbour_spaces(self, space: Cube) -> list[Cube]:
        return [
            space for space in [
                Cube(space.x - 1, space.y, space.z),
                Cube(space.x + 1, space.y, space.z),
                Cube(space.x, space.y - 1, space.z),
                Cube(space.x, space.y + 1, space.z),
                Cube(space.x, space.y, space.z - 1),
                Cube(space.x, space.y, space.z + 1),
            ]
            if (
                space.x >= self.limits.x[0] - 1 and
                space.x <= self.limits.x[1] + 1 and
                space.y >= self.limits.y[0] - 1 and
                space.y <= self.limits.y[1] + 1 and
                space.z >= self.limits.z[0] - 1 and
                space.z <= self.limits.z[1] + 1
            )
        ]
