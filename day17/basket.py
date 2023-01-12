from typing import Optional

import numpy as np

from day17.figure import Figure


class Basket:
    INITIAL_CAPACITY = 16
    MIN_SLACK_SIZE = 10

    def __init__(self, width: int):
        self._width = width
        self._height = 0
        self._capacity = self.INITIAL_CAPACITY
        self._array = np.zeros([self._capacity, self.width])

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def array(self):
        view = self._array[:self.height]
        view.flags.writeable = False
        return view

    def _resize_capacity(self) -> None:
        if self._height + self.MIN_SLACK_SIZE > self._capacity:
            self._capacity *= 2
            new_array = np.zeros([self._capacity, self._width])
            new_array[:self._height] = self._array[:self._height]
            self._array = new_array

    def add_figure(self, figure: Figure):
        array_slice = self._array[
            figure.position.y: figure.position.y + figure.height,
            figure.position.x: figure.position.x + figure.width
        ]
        assert figure.shape.shape == array_slice.shape
        assert np.max(figure.shape + array_slice) <= 1  # type: ignore
        array_slice += figure.shape
        if figure.position.y + figure.height > self._height:
            self._height = figure.position.y + figure.height
            self._resize_capacity()

    def check_figure_collision(self, figure: Figure) -> bool:
        array_slice = self._array[
            figure.position.y: figure.position.y + figure.height,
            figure.position.x: figure.position.x + figure.width
        ]
        assert figure.shape.shape == array_slice.shape
        return bool(np.max(figure.shape + array_slice) > 1)  # type: ignore

    def draw(self, tail_size: int = 20, current_figure: Optional[Figure] = None) -> None:
        for y, line in zip(range(tail_size - 1, -1, -1), reversed(self._array[:20])):
            print('|', end='')
            for x, char in enumerate(line):
                if current_figure is not None and \
                        x >= current_figure.position.x and x < current_figure.position.x + current_figure.width and \
                        y >= current_figure.position.y and y < current_figure.position.y + current_figure.height and \
                        current_figure.shape[y - current_figure.position.y, x - current_figure.position.x] == 1:
                    print('@', end='')
                elif char == 1:
                    print('#', end='')
                else:
                    print('.', end='')
            print('|')
        print('+-------+')
