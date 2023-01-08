from dataclasses import dataclass


@dataclass(order=True)
class HalfInterval:
    start: int
    end: int
