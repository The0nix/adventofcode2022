import itertools
from collections.abc import Iterable
from collections import Counter

from solution import SolutionFromLines
from day18.cube import Cube, CubeSide
from day18.lava_droplet import LavaDroplet


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        cubes = (Cube(*[int(coord) for coord in line.split(',')]) for line in lines)
        lava_droplet = LavaDroplet(cubes)
        if self.part == 1:
            result = lava_droplet.calculate_surface_area()
        else:
            result = lava_droplet.calculate_outer_surface_area()
        return result
