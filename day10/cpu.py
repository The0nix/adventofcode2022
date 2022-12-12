class CPU:
    def __init__(self) -> None:
        self._x = 1
        self._current_cycle = 0

    @property
    def x(self) -> int:
        return self._x

    @property
    def current_cycle(self) -> int:
        return self._current_cycle

    def addx(self, value: int) -> None:
        self._x += value
        self._current_cycle += 2

    def noop(self) -> None:
        self._current_cycle += 1
