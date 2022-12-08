from pathlib import Path
from enum import Enum

import click

from filetree import FileTree


class STATE(Enum):
    INPUT_COMMAND = 1
    READ_LS_OUTPUT = 2


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        state = STATE.INPUT_COMMAND
        tree = FileTree()
        for line in f:
            line = line.strip()
            if state == STATE.READ_LS_OUTPUT:
                if line.startswith('$'):
                    state = STATE.INPUT_COMMAND
                else:
                    size, name = line.split()
                    if size == 'dir':
                        tree.add_directory(name)
                    else:
                        tree.add_file(name, int(size))
            if state == STATE.INPUT_COMMAND:
                command, *args = line[2:].split()
                if command == 'cd':
                    tree.cd(args[0])
                elif command == 'ls':
                    state = STATE.READ_LS_OUTPUT
                    continue

    total_space = 70000000
    space_needed = 30000000
    minimal_needed_space = space_needed - (total_space - tree.size)
    result = min(d.size for d in tree.traverse_all_directories() if d.size >= minimal_needed_space)
    print(result)


if __name__ == '__main__':
    main()
