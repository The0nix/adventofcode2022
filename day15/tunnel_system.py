from collections.abc import Iterable
from typing import Optional

from tqdm.auto import tqdm

from day15.half_interval import HalfInterval
from day15.position import Position
from day15.sensor import Sensor


class NoBeaconError(Exception):
    pass


class TunnelSystem:
    def __init__(self, lines: Iterable[str]) -> None:
        self._sensors: list[Sensor] = []
        for line in lines:
            self._sensors.append(Sensor(line))

    def calculate_coverage(self, y: int) -> int:
        intervals: list[HalfInterval] = [sensor.calculate_intersection(y) for sensor in self._sensors]
        intervals.sort()
        current_size = 0
        current_start, current_end = intervals[0].start, intervals[0].end
        for interval in intervals[1:]:
            if interval.start > current_end:
                current_size += current_end - current_start
                current_start, current_end = interval.start, interval.end
            else:
                current_end = max(current_end, interval.end)
        current_size += current_end - current_start
        return current_size

    def _get_first_empty(self, y: int, interval_limit: HalfInterval) -> Optional[int]:
        intervals: list[HalfInterval] = [sensor.calculate_intersection(y, ignore_beacons=True) for sensor in self._sensors]
        for i in range(len(intervals)):
            if interval_limit is not None:
                if intervals[i].start < interval_limit.start:
                    intervals[i].start = interval_limit.start
                if intervals[i].end > interval_limit.end:
                    intervals[i].end = interval_limit.end
                if intervals[i].start > intervals[i].end:
                    intervals[i] = None  # type: ignore
        intervals = [interval for interval in intervals if interval is not None]
        intervals.sort()
        current_start, current_end = intervals[0].start, intervals[0].end
        if current_start > 0:
            return 0
        for interval in intervals[1:]:
            if interval.start > current_end:
                return current_end
            else:
                current_end = max(current_end, interval.end)
        return None


    def locate_beacon(self, max_x: int, max_y: int) -> Position:
        for y in tqdm(range(max_y + 1)):
            first_empty = self._get_first_empty(y, interval_limit=HalfInterval(0, max_x + 1))
            if first_empty is not None:
                return Position(first_empty, y)
        raise NoBeaconError()

