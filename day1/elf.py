class Elf:
    def __init__(self):
        self._items_weights: list[int] = []
        self._total_calories = 0

    @property
    def total_calories(self):
        return self._total_calories

    def add_item(self, weight: int) -> None:
        self._items_weights.append(weight)
        self._total_calories += weight
