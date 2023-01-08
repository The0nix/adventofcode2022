from collections.abc import Iterable

from solution import SolutionFromLines
from day1.elf import Elf


class DaySolution(SolutionFromLines[int]):
    def solve_impl(self, lines: Iterable[str]) -> int:
        if self.part == 1:
            max_calories = -1
            current_elf = Elf()
            for line in lines:
                if line:
                    current_elf.add_item(int(line))
                else:
                    if current_elf.total_calories > max_calories:
                        max_calories = current_elf.total_calories
                    current_elf = Elf()
            return(max_calories)
        else:
            max_calories = [-1, -1, -1]
            current_elf = Elf()
            for line in lines:
                if line:
                    current_elf.add_item(int(line))
                else:
                    if current_elf.total_calories > max_calories[-1]:
                        max_calories[-1] = current_elf.total_calories
                        max_calories.sort(reverse=True)
                    current_elf = Elf()
            return sum(max_calories)
