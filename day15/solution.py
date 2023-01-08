from collections.abc import Iterable

from solution import SolutionFromLines
from day15.tunnel_system import TunnelSystem


class DaySolution(SolutionFromLines[int]):
    def __init__(self, part: int, *, y: int = 2_000_000, interval_end: int = 4_000_000) -> None:
        super().__init__(part)
        self.y = y
        self.interval_end = interval_end

    def solve_impl(self, lines: Iterable[str]) -> int:
        tunnel_system = TunnelSystem(lines)
        if self.part == 1:
            result = tunnel_system.calculate_coverage(self.y)
        else:
            beacon_position = tunnel_system.locate_beacon(self.interval_end, self.interval_end)
            print(beacon_position)
            result = beacon_position.x * 4_000_000 + beacon_position.y
        return result
