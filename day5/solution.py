import re
from pathlib import Path

from solution import Solution
from day5.stacks import Stacks

PARSE_RE = re.compile(r'move (?P<number>\d+) from (?P<from_index>\d+) to (?P<to_index>\d+)')


class DaySolution(Solution[str]):
    def solve(self, input_file_path: Path) -> str:
        with open(input_file_path) as f:
            if self.part == 1:
                stacks = Stacks.from_lines(f)
                stacks.print_drawing()
                f.readline()
                for line in f:
                    parsed_command = PARSE_RE.match(line.strip())
                    if parsed_command:
                        kwargs = {k: int(v) for k, v in parsed_command.groupdict().items()}
                        stacks.move(**kwargs)
                stacks.print_drawing()
                return ''.join(stacks.get_tops())
            else:
                stacks = Stacks.from_lines(f)
                stacks.print_drawing()
                f.readline()
                for line in f:
                    parsed_command = PARSE_RE.match(line.strip())
                    if parsed_command:
                        kwargs = {k: int(v) for k, v in parsed_command.groupdict().items()}
                        stacks.move(**kwargs, reverse=False)
                stacks.print_drawing()
                return ''.join(stacks.get_tops())
