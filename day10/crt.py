from typing import Optional, Iterable

from cpu import CPU


class FrameEnded(Exception):
    pass


class CRT:
    def __init__(self, cpu: Optional[CPU] = None, width: int = 40, height: int = 6) -> None:
        self._width = width
        self._height = height
        self._screen_size = self._width * self._height
        self._cpu = cpu if cpu is not None else CPU()
        self._image_buffer: list[list[str]] = [['' for _ in range(self._width)] for _ in range(self._height)]
        self._current_cycle = 0

    def _draw_pixel(self, sprite_position: int) -> None:
        if self._current_cycle >= self._screen_size:
            raise FrameEnded
        current_row = self._current_cycle // self._width
        current_column = self._current_cycle % self._width
        if sprite_position - 1 <= current_column and sprite_position + 1 >= current_column:
            self._image_buffer[current_row][current_column] = '#'
        else:
            self._image_buffer[current_row][current_column] = ' '
        self._current_cycle += 1

    def execute_commands(self, commands: Iterable[str]) -> None:
        for line in commands:
            sprite_position = self._cpu.x
            command, *args = line.strip().split()
            if command == 'noop':
                self._cpu.noop()
            elif command == 'addx':
                self._cpu.addx(int(args[0]))
            else:
                raise ValueError(f'Unknown command: {command}')
            while self._current_cycle < self._cpu.current_cycle:
                self._draw_pixel(sprite_position)

    def draw_image(self) -> None:
        print('\n'.join(''.join(column for column in row) for row in self._image_buffer))
