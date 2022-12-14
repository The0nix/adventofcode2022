from pathlib import Path

import click

from packet import Packet


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    packets: list[Packet] = []
    divider_packets = [Packet('[[2]]'), Packet('[[6]]')]
    with open(input) as f:
        for line in f:
            if line.strip():
                packets.append(Packet(line.strip()))
    packets.extend(divider_packets)
    packets.sort()
    result = (packets.index(divider_packets[0]) + 1) * (packets.index(divider_packets[1]) + 1)
    print(result)


if __name__ == '__main__':
    main()
