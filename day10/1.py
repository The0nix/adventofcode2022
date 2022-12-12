from pathlib import Path

import click

from cpu import CPU

CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220]


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        cycles_to_check = list(reversed(CYCLES_TO_CHECK))
        cpu = CPU()
        signal_strengths: list[int] = []
        for line in f:
            if not cycles_to_check:
                break
            previous_x = cpu.x
            command, *args = line.strip().split()
            if command == 'noop':
                cpu.noop()
            elif command == 'addx':
                cpu.addx(int(args[0]))
            else:
                raise ValueError(f'Unknown command: {command}')
            if cpu.current_cycle >= cycles_to_check[-1]:
                signal_strengths.append(previous_x * cycles_to_check[-1])
                cycles_to_check.pop()
        print(signal_strengths)
        print(sum(signal_strengths))


if __name__ == '__main__':
    main()
