import itertools
from pathlib import Path

import click
from unique_counting_limited_queue import UniqueCountingLimitedQueue


@click.command()
@click.argument('input', type=Path)
def main(input: Path) -> None:
    with open(input) as f:
        uclq: UniqueCountingLimitedQueue[str] = UniqueCountingLimitedQueue(4)
        for i in itertools.count(1):
            symbol = f.read(1)
            if symbol == '\n':
                break
            uclq.append(symbol)
            if uclq.n_unique == 14:
                print(i)
                break

        
    


if __name__ == '__main__':
    main()
