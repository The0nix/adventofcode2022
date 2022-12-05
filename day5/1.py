from pathlib import Path

import click
import parse

from stacks import Stacks

PARSE_STRING = 'move {number} from {from_index} to {to_index}'


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        stacks = Stacks.from_lines(f)
        stacks.print_drawing()
        f.readline()
        for line in f:
            parsed_command = parse.parse(PARSE_STRING, line.strip())
            parsed_command = {key: int(value) for key, value in parsed_command.named.items()}
            stacks.move(**parsed_command)
    stacks.print_drawing()
    print(''.join(stacks.get_tops()))


if __name__ == '__main__':
    main()
