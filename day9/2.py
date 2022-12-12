from pathlib import Path

import click
from rope import Rope, Direction, Position

COMMAND_TO_DIRECTION = {
    'U': Direction.UP,
    'D': Direction.DOWN,
    'L': Direction.LEFT,
    'R': Direction.RIGHT,
}


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        rope = Rope(9)
        unique_tail_positions = {Position()}
        for line in f:
            command, number = line.strip().split()
            for _ in range(int(number)):
                new_tail_position = rope.move_head(COMMAND_TO_DIRECTION[command])
                unique_tail_positions.add(new_tail_position)
        print(len(unique_tail_positions))


if __name__ == '__main__':
    main()
