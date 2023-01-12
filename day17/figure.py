import abc

import numpy as np

from day17.position import Position


class Figure(abc.ABC):
    _shape_list: list[list[int]] = [[]]

    def __init__(self, position: Position = Position(0, 0)):
        self._position = position
        self._shape = np.array(self._shape_list)

    @property
    def shape(self):
        view = self._shape.view()
        view.flags.writeable = False
        return view

    @property 
    def position(self) -> Position:
        return self._position

    @property
    def height(self) -> int:
        return self._shape.shape[0]

    @property
    def width(self) -> int:
        return self._shape.shape[1]

    def shift_left(self) -> None:
        self._position += (-1, 0)

    def shift_right(self) -> None:
        self._position += (1, 0)

    def shift_up(self) -> None:
        self._position += (0, 1)

    def shift_down(self) -> None:
        self._position += (0, -1)

class HorizontalLine(Figure):
    _shape_list = [
        [1, 1, 1, 1],
    ]


class Cross(Figure):
    _shape_list = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ]


class J(Figure):
    _shape_list = [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ]


class VerticalLine(Figure):
    _shape_list = [
        [1],
        [1],
        [1],
        [1],
    ]


class Square(Figure):
    _shape_list = [
        [1, 1],
        [1, 1],
    ]
