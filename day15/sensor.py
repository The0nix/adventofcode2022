import re

from day15.half_interval import HalfInterval
from day15.position import Position


class Sensor:
    PARSER_RE = re.compile(
        r'Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): ' \
        r'closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)'
    )

    def __init__(self, line: str) -> None:
        match = self.PARSER_RE.match(line)
        assert match is not None
        match_dict = match.groupdict()

        self._position = Position(int(match_dict['sensor_x']), int(match_dict['sensor_y']))
        self._beacon_position = Position(int(match_dict['beacon_x']), int(match_dict['beacon_y']))

    def calculate_intersection(self, y: int, ignore_beacons: bool = False) -> HalfInterval:
        distance_to_beacon = (
            abs(self._beacon_position.x - self._position.x) +
            abs(self._beacon_position.y - self._position.y)
        )
        t_leg_length = distance_to_beacon - abs(self._position.y - y)
        if t_leg_length < 0:
            return HalfInterval(0, 0)
        interval = HalfInterval(self._position.x - t_leg_length, self._position.x + t_leg_length + 1)
        if not ignore_beacons:
            if self._beacon_position.y == y:
                if self._beacon_position.x == interval.start:
                    interval.start += 1
                elif self._beacon_position.x == interval.end - 1:
                    interval.end -= 1
        return interval
