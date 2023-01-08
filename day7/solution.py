from collections.abc import Iterable
from enum import Enum

from solution import SolutionFromLines
from day7.filetree import FileTree


class STATE(Enum):
    INPUT_COMMAND = 1
    READ_LS_OUTPUT = 2


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        state = STATE.INPUT_COMMAND
        tree = FileTree()
        for line in lines:
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

        if self.part == 1:
            return sum(d.size for d in tree.traverse_all_directories() if d.size <= 100000)
        else:
            total_space = 70000000
            space_needed = 30000000
            minimal_needed_space = space_needed - (total_space - tree.size)
            return min(d.size for d in tree.traverse_all_directories() if d.size >= minimal_needed_space)
