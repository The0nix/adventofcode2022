import importlib
from pathlib import Path
from typing import Optional

import click


@click.command()
@click.argument('day', type=int)
@click.argument('part', type=int)
@click.option('--input', type=Path)
def main(day: int, part: int, input: Optional[Path]) -> None:
    day_solution_module = importlib.import_module(f'day{day}.solution')
    solution = day_solution_module.DaySolution(part)
    if input is None:
        input = Path(f'day{day}') / 'inputs' / 'input.txt'
    print(solution.solve(input))


if __name__ == '__main__':
    main()
