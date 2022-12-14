from pathlib import Path

import click

from packet import Packet


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    proper_order: list[int] = []
    with open(input) as f:
        iterator = (line.strip() for line in f)
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
    print(proper_order)
    print(sum(proper_order))


if __name__ == '__main__':
    main()
