from __future__ import annotations

class CubeSide:
    def __init__(self, x: float, y: float, z: float) -> None:
        self._x = int(x * 2)
        self._y = int(y * 2)
        self._z = int(z * 2)
    
    def __hash__(self) -> int:
        return hash((self._x, self._y, self._z))
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, CubeSide):
            return self._x == other._x and self._y == other._y and self._z == other._z
        return NotImplemented
    
    def __repr__(self) -> str:
        return f'CubeSide({self._x / 2}, {self._y / 2}, {self._z / 2})'


class Cube:
    class NoCommonSidesError(Exception):
        pass

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def sides(self) -> tuple[CubeSide, CubeSide, CubeSide, CubeSide, CubeSide, CubeSide]:
        return (
            CubeSide(self.x + .5, self.y, self.z),
            CubeSide(self.x - .5, self.y, self.z),
            CubeSide(self.x, self.y + .5, self.z),
            CubeSide(self.x, self.y - .5, self.z),
            CubeSide(self.x, self.y, self.z + .5),
            CubeSide(self.x, self.y, self.z - .5),
        )

    def get_common_side(self, other: Cube) -> CubeSide:
        coordinate_diffs = (other.x - self.x, other.y - self.y, other.z - self.z)
        if not (
            len([diff for diff in coordinate_diffs if diff == 0]) == 2 and 
            len([diff for diff in coordinate_diffs if abs(diff) == 1]) == 1
        ):
            raise self.NoCommonSidesError(f'{self} and {other}')
        return CubeSide(
            self.x + coordinate_diffs[0] / 2,
            self.y + coordinate_diffs[1] / 2,
            self.z + coordinate_diffs[2] / 2,
        )

    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Cube):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return NotImplemented

    def __repr__(self) -> str:
        return f'Cube({self.x}, {self.y}, {self.z})'
