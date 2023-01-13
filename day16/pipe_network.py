# pyright: reportUnknownArgumentType=false, reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false, reportGeneralTypeIssues=false
import math
import functools
import itertools
from collections.abc import Iterable
from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

from day16.network_node import NetworkNode


class PipeNetwork:
    def __init__(self, lines: Iterable[str]) -> None:
        self._nodes: dict[str, NetworkNode] = {}
        for line in lines:
            node = NetworkNode(line)
            self._nodes[node.name] = node
        self._FW = self._get_floyd_warshall()

    @functools.cache
    def _get_best_pressure_recursive(
        self,
        current_node: str,
        time_left: int,
        closed_nodes: frozenset[str],
        open_nodes: frozenset[str],
    ) -> int:
        if time_left <= 0:
            return 0
        pressure_released = sum(self._nodes[node].flow_rate for node in open_nodes)
        if not closed_nodes:
            return pressure_released * time_left
        possible_results: list[int] = []
        for neighbour in self._FW[current_node]:
            if neighbour in closed_nodes and self._FW[current_node][neighbour] < time_left:
                possible_results.append(
                    pressure_released * (self._FW[current_node][neighbour] + 1) +
                    self._get_best_pressure_recursive(
                        neighbour,
                        time_left - self._FW[current_node][neighbour] - 1,
                        closed_nodes - {neighbour},
                        open_nodes | {neighbour},
                    )
                )
        if not possible_results:
            return pressure_released * time_left
        return max(possible_results)

    def get_best_pressure(self, time: int = 30):
        return self._get_best_pressure_recursive('AA', time, frozenset(self._FW.keys()), frozenset())

    def get_best_pressure_with_elephant(self, time: int = 26):
        best_pressure = 0
        for group_size in tqdm(range(1, len(self._FW) // 2 + 1), desc='Group size'):
            for group in tqdm(
                itertools.combinations(self._FW.keys(), group_size), 
                total=math.comb(len(self._FW), group_size)
            ):
                my_group: frozenset[str] = frozenset(group)
                elephant_group: frozenset[str] = frozenset(node for node in self._FW if node not in my_group)
                candidate_pressure = \
                    self._get_best_pressure_recursive('AA', time, my_group, frozenset()) + \
                    self._get_best_pressure_recursive('AA', time, elephant_group, frozenset())

                if candidate_pressure > best_pressure:
                    best_pressure = candidate_pressure
        return best_pressure

    def get_networkx_graph(self) -> nx.Graph:
        graph = nx.Graph()
        for node in self._nodes.values():
            graph.add_node(node.name, flow_rate=node.flow_rate)
            graph.add_node(node.name, flow_rate=node.flow_rate)
        for node in self._nodes.values():
            for neighbour in node.tunnels:
                graph.add_edge(node.name, neighbour)
        return graph

    def _get_floyd_warshall(self) -> dict[str, dict[str, int]]:
        graph = self.get_networkx_graph()
        FW: dict[str, defaultdict[str, float]] = nx.floyd_warshall(graph)
        FW = {k: v for k, v in FW.items() if self._nodes[k].flow_rate > 0 or self._nodes[k].name == 'AA'}  # type: ignore
        for src in FW:
            FW[src] = {k: int(v) for k, v in FW[src].items() if k != src and (self._nodes[k].flow_rate > 0 or self._nodes[k].name == 'AA')}
        return FW

    def draw_graph(self) -> None:
        nx.draw(
            self.get_networkx_graph(), with_labels=True, font_weight='bold', node_size=2000,
            labels={node.name: f'{node.name}: {node.flow_rate}' for node in self._nodes.values()}
        )
        plt.show()
