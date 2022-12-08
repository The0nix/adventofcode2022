from collections import deque, Counter
from typing import TypeVar, Generic


T = TypeVar('T')


class UniqueCountingLimitedQueue(Generic[T]):
    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._contents: deque[T] = deque()  # No maxlen because we want to contorl it manually
        self._counter: Counter[T] = Counter()

    def append(self, value: T) -> None:
        self._contents.append(value)
        self._counter[value] += 1
        if len(self._contents) > self._limit:
            deleted = self._contents.popleft()
            self._counter[deleted] -= 1
            if self._counter[deleted] == 0:
                del self._counter[deleted]

    @property
    def n_unique(self) -> int:
        return len(self._counter)
