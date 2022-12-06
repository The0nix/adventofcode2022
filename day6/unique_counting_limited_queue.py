from collections import deque, Counter


class UniqueCountingLimitedQueue:
    def __init__(self, limit) -> None:
        self._limit = limit
        self._contents = deque()  # No maxlen because we want to contorl it manually
        self._counter = Counter()

    def append(self, value):
        self._contents.append(value)
        self._counter[value] += 1
        if len(self._contents) > self._limit:
            deleted = self._contents.popleft()
            self._counter[deleted] -= 1
            if self._counter[deleted] == 0:
                del self._counter[deleted]

    @property
    def n_unique(self):
        return len(self._counter)
