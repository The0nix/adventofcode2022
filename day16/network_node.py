import re


class ParseError(Exception):
    pass


class NetworkNode:
    PARSE_RE = re.compile(
        r'Valve (?P<name>[A-Z]{2}) has flow rate=(?P<flow_rate>\d+); tunnels? leads? to valves? (?P<tunnels>.+)'
    )

    def __init__(self, line: str) -> None:
        match = self.PARSE_RE.match(line)
        if match is None:
            raise ParseError(f'Wrong format for parsing a network node: "{line}"')
        match_dict = match.groupdict()
        self._open = False
        self._name = match_dict['name']
        self._flow_rate = int(match_dict['flow_rate'])
        self._tunnels: list[str] = match_dict['tunnels'].split(', ')

    def open_valve(self) -> None:
        self._open = True

    def is_valve_open(self) -> bool:
        return self._open

    @property
    def name(self) -> str:
        return self._name

    @property
    def flow_rate(self) -> int:
        return self._flow_rate

    @property
    def tunnels(self) -> tuple[str]:
        return tuple(self._tunnels)
