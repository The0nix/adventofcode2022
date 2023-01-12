# pyright: reportPrivateUsage=false
import numpy as np

from day17.basket import Basket
from day17.figure import Cross, VerticalLine
from day17.position import Position


class TestBasket:
    def setup_method(self):
        self.basket = Basket(width=7)

    def test_width(self):
        assert Basket(10).width == 10

    def test_height(self):
        assert self.basket.height == 0
        self.basket.add_figure(Cross(Position(0, 0)))
        assert self.basket.height == 3
        self.basket.add_figure(Cross(Position(3, 3)))
        assert self.basket.height == 6
        self.basket.add_figure(VerticalLine(Position(3, 5)))
        assert self.basket.height == 9

    def test_add_figure(self):
        self.basket.add_figure(Cross(Position(0, 0)))
        assert np.array_equal(  # type: ignore
            self.basket.array,
            np.array([
                [0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0],
            ])
        )

    def test_check_figure_collision(self):
        assert not self.basket.check_figure_collision(Cross(Position(0, 0)))

        self.basket.add_figure(Cross(Position(0, 0)))
        assert self.basket.check_figure_collision(Cross(Position(0, 0)))
        assert self.basket.check_figure_collision(Cross(Position(0, 1)))
        assert self.basket.check_figure_collision(Cross(Position(1, 0)))
        assert self.basket.check_figure_collision(Cross(Position(1, 1)))
        assert not self.basket.check_figure_collision(Cross(Position(1, 2)))
        assert not self.basket.check_figure_collision(Cross(Position(2, 1)))
        assert not self.basket.check_figure_collision(Cross(Position(2, 2)))
        assert not self.basket.check_figure_collision(Cross(Position(3, 2)))
        assert not self.basket.check_figure_collision(Cross(Position(2, 3)))
        assert not self.basket.check_figure_collision(Cross(Position(3, 3)))

        self.basket.add_figure(Cross(Position(3, 3)))
        assert self.basket.check_figure_collision(Cross(Position(3, 3)))
