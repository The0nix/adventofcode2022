from collections.abc import Iterable

from solution import SolutionFromLines
from day13.packet import Packet


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        if self.part == 1:
            proper_order: list[int] = []
            iterator = iter(lines)
            index = 1
            while True:
                try:
                    left = Packet(next(iterator))
                    right = Packet(next(iterator))
                    if left < right:
                        proper_order.append(index)
                    next(iterator)
                except StopIteration:
                    break
                index += 1
            return sum(proper_order)
        else:
            packets: list[Packet] = []
            divider_packets = [Packet('[[2]]'), Packet('[[6]]')]
            for line in lines:
                if line.strip():
                    packets.append(Packet(line.strip()))
            packets.extend(divider_packets)
            packets.sort()
            result = (packets.index(divider_packets[0]) + 1) * (packets.index(divider_packets[1]) + 1)
            return result
