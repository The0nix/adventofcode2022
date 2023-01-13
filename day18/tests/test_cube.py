import pytest

from day18.cube import Cube, CubeSide


def test_sides():
    cube = Cube(0, 0, 0)
    assert set(cube.sides) == set([
        CubeSide(.5, 0, 0),
        CubeSide(-.5, 0, 0),
        CubeSide(0, .5, 0),
        CubeSide(0, -.5, 0),
        CubeSide(0, 0, .5),
        CubeSide(0, 0, -.5),
    ])

    x, y, z = 50, 42, -14
    cube = Cube(x, y, z)
    assert set(cube.sides) == set([
        CubeSide(x+.5, y, z),
        CubeSide(x-.5, y, z),
        CubeSide(x, y+.5, z),
        CubeSide(x, y-.5, z),
        CubeSide(x, y, z+.5),
        CubeSide(x, y, z-.5),
    ])


def test_common_side():
    assert Cube(0, 0, 0).get_common_side(Cube(0, 0, 1)) == CubeSide(0, 0, 0.5)
    assert Cube(0, 1, 1).get_common_side(Cube(0, 2, 1)) == CubeSide(0, 1.5, 1)
    with pytest.raises(Cube.NoCommonSidesError):
        Cube(0, 0, 0).get_common_side(Cube(0, 1, 1))

