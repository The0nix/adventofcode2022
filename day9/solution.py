from collections.abc import Iterable

from solution import SolutionFromLines
from day9.rope import Rope, Direction, Position


COMMAND_TO_DIRECTION = {
    'U': Direction.UP,
    'D': Direction.DOWN,
    'L': Direction.LEFT,
    'R': Direction.RIGHT,
}


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        rope = Rope(1 if self.part == 1 else 9)
        unique_tail_positions = {Position()}
        for line in lines:
            command, number = line.split()
            for _ in range(int(number)):
                new_tail_position = rope.move_head(COMMAND_TO_DIRECTION[command])
                unique_tail_positions.add(new_tail_position)
        return len(unique_tail_positions)

