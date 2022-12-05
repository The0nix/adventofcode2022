from __future__ import annotations


class Interval:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def __contains__(self, other: Interval) -> bool:
        return other.start >= self.start and other.end <= self.end

    def __and__(self, other: Interval) -> Interval:
        return Interval(max(self.start, other.start), min(self.end, other.end))

    def __len__(self) -> int:
        return max(0, self.end - self.start + 1)

    @classmethod
    def from_string(cls, string, delimiter='-') -> Interval:
        start, end = string.split(delimiter)
        return cls(int(start), int(end))
