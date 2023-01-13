from collections.abc import Iterable
from typing import Type, Optional

from day17.position import Position
from day17.figure import Figure
from day17.basket import Basket


class RockFall:
    START_OFFSET_X = 2
    START_OFFSET_Y = 3

    def __init__(self, basket: Basket, figure_classes: Iterable[Type[Figure]], directions: Iterable[str]) -> None:
        self.basket = basket
        self.figure_classes = list(figure_classes)
        self.figure_index = 0
        self.directions = list(directions)
        self.direction_index = 0
        self.current_figure: Optional[Figure] = None

    def perform_fall(self) -> None:
        new_figure_position = Position(self.START_OFFSET_X, self.basket.height + self.START_OFFSET_Y)
        self.current_figure = self.figure_classes[self.figure_index](new_figure_position)
        self.figure_index = (self.figure_index + 1) % len(self.figure_classes)
        while True:
            came_to_rest = self._perform_iteration()
            if came_to_rest:
                break
            
    def _perform_iteration(self) -> bool:
        assert self.current_figure is not None
        figure = self.current_figure
        direction = self.directions[self.direction_index]
        self.direction_index = (self.direction_index + 1) % len(self.directions)

        if direction == '<':
            if figure.position.x > 0:
                figure.shift_left()
                if self.basket.check_figure_collision(figure):
                    figure.shift_right()
        elif direction == '>':
            if figure.position.x + figure.width <= self.basket.width - 1:
                figure.shift_right()
                if self.basket.check_figure_collision(figure):
                    figure.shift_left()
        else:
            raise ValueError(f'Incorrect direction: "{direction}"')
        figure.shift_down()
        if figure.position.y < 0 or self.basket.check_figure_collision(figure):
            figure.shift_up()
            self.basket.add_figure(figure)
            return True
        return False
    
    @property
    def state(self) -> tuple[int, int, str]:
        return (
            self.figure_index,
            self.direction_index,
            str(self.basket.array[-5:]),
        )
