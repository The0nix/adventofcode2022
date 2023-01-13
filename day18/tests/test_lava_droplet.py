# pyright: reportPrivateUsage=false
from pathlib import Path

from day18.cube import Cube
from day18.lava_droplet import LavaDroplet, LavaDropletLimits


def test_n_cubes():
    lava_droplet = LavaDroplet([
        Cube(0, 0, 0),
        Cube(0, 0, 1),
        Cube(0, 3, 0),
    ])
    assert lava_droplet.n_cubes == 3


def test_limits():
    lava_droplet = LavaDroplet([
        Cube(50, 10, -100),
        Cube(-30, 25, -50),
        Cube(-29, 15, -10),
    ])
    assert lava_droplet.limits == LavaDropletLimits(
        (-30, 50),
        (10, 25),
        (-100, -10),
    )


def test_surface_area():
    with open(Path('day18') / 'inputs' / 'input_test.txt') as f:
        lines = (line.strip() for line in f)
        cubes = (Cube(*[int(coord) for coord in line.split(',')]) for line in lines)
        lava_droplet = LavaDroplet(cubes)
    surface_area = lava_droplet.calculate_surface_area()
    assert surface_area == 64


def test_outer_surface_area():
    with open(Path('day18') / 'inputs' / 'input_test.txt') as f:
        lines = (line.strip() for line in f)
        cubes = (Cube(*[int(coord) for coord in line.split(',')]) for line in lines)
        lava_droplet = LavaDroplet(cubes)
    surface_area = lava_droplet.calculate_outer_surface_area()
    assert surface_area == 58

def test_get_neighbour_spaces():
    lava_droplet = LavaDroplet([
        Cube(0, 0, 0),
        Cube(0, 0, 1),
        Cube(0, 3, 0),
    ])
    neighbour_spaces = lava_droplet._get_neighbour_spaces(Cube(0, 0, 0))
    assert set(neighbour_spaces) == set([
        Cube(-1, 0, 0),
        Cube(1, 0, 0),
        Cube(0, -1, 0),
        Cube(0, 1, 0),
        Cube(0, 0, -1),
        Cube(0, 0, 1),
    ])

    neighbour_spaces = lava_droplet._get_neighbour_spaces(Cube(-1, -1, -1))
    assert set(neighbour_spaces) == set([
        Cube(0, -1, -1),
        Cube(-1, 0, -1),
        Cube(-1, -1, 0),
    ])
