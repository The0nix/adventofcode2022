import re
from pathlib import Path

import click

from stacks import Stacks

PARSE_RE = re.compile(r'move (?P<number>\d+) from (?P<from_index>\d+) to (?P<to_index>\d+)')


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        stacks = Stacks.from_lines(f)
        stacks.print_drawing()
        f.readline()
        for line in f:
            parsed_command = PARSE_RE.match(line.strip())
            if parsed_command:
                kwargs = {k: int(v) for k, v in parsed_command.groupdict().items()}
                stacks.move(**kwargs, reverse=False)
    stacks.print_drawing()
    print(''.join(stacks.get_tops()))


if __name__ == '__main__':
    main()
