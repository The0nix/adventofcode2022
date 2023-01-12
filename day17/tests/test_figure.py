import pytest
import numpy as np

from day17.position import Position
from day17.figure import VerticalLine, HorizontalLine, Cross

def test_shifts():
    vertical_line = VerticalLine()
    assert vertical_line.position == Position(0, 0)
    vertical_line.shift_right()
    assert vertical_line.position == Position(1, 0)
    vertical_line.shift_left()
    assert vertical_line.position == Position(0, 0)
    vertical_line.shift_down()
    assert vertical_line.position == Position(0, -1)
    vertical_line.shift_up()
    assert vertical_line.position == Position(0, 0)

def test_sizes():
    assert VerticalLine().width == 1
    assert VerticalLine().height == 4
    assert HorizontalLine().width == 4
    assert HorizontalLine().height == 1
    assert Cross().width == 3
    assert Cross().height == 3

def test_shape_view():
    figure = Cross()
    assert np.array_equal(  # type: ignore
        figure.shape,
        np.array([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ])
    )
    shape = figure.shape
    with pytest.raises(ValueError):
        shape += 1
