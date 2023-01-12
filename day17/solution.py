from typing import Any
from pathlib import Path

from tqdm.auto import tqdm

from solution import Solution
from day17.figure import HorizontalLine, Cross, J, VerticalLine, Square
from day17.basket import Basket
from day17.rockfall import RockFall


class DaySolution(Solution[int]):
    def solve(self, input_file_path: Path) -> int:
        simulation_length = 2022 if self.part == 1 else 1_000_000_000_000
        rockfall = RockFall(
            basket=Basket(7),
            figure_classes=[HorizontalLine, Cross, J, VerticalLine, Square],
            directions=input_file_path.read_text().strip(),
        )

        iteration = 0
        cycled = False
        state_to_iteration_and_height: dict[Any, tuple[int, int]] = {}
        additional_height = 0
        with tqdm(total=simulation_length) as pbar:
            while iteration < simulation_length:
                if not cycled:
                    if rockfall.state in state_to_iteration_and_height:
                        cycled = True
                        cycle_start_iteration, cycle_start_height = state_to_iteration_and_height[rockfall.state]
                        cycle_iterations = iteration - cycle_start_iteration
                        cycle_height = rockfall.basket.height - cycle_start_height
                        cycles_to_skip = (simulation_length - iteration) // cycle_iterations
                        additional_height = cycles_to_skip * cycle_height
                        iteration += cycles_to_skip * cycle_iterations
                        pbar.update(cycles_to_skip * cycle_iterations)
                    else:
                        state_to_iteration_and_height[rockfall.state] = (iteration, rockfall.basket.height)
                rockfall.perform_fall()
                iteration += 1
                pbar.update(1)
        return rockfall.basket.height + additional_height
