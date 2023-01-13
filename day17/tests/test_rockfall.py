# pyright: reportPrivateUsage=false
from pathlib import Path


from day17.basket import Basket
from day17.figure import HorizontalLine, Cross, J, VerticalLine, Square
from day17.rockfall import RockFall


class TestRockFall:
    def setup_method(self):
        directions_str = (Path('day17') / 'inputs' / 'input_test.txt').read_text().strip()
        self.rockfall = RockFall(
            basket=Basket(width=7),
            figure_classes=[HorizontalLine, Cross, J, VerticalLine, Square],
            directions=directions_str
        )

    def test_height(self):
        for _ in range(2022):
            self.rockfall.perform_fall()
        assert self.rockfall.basket.height == 3068
