"""https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, TypeVar, Generic
from heapq import heappush, heappop


T = TypeVar("T")
V = int  # vertex id
W = int  # weight

INF = 1 << 30


@dataclass(order=True)
class Ord(Generic[T]):
    """Custom comparable class"""

    key: T = field(compare=True)
    value: Any = field(compare=False)


@dataclass(order=True)
class VW:
    """shorthand for Vertex and Weight"""

    vertex: int = field(compare=False)
    weight: int


@dataclass(order=True)
class VWD(VW):
    """shorthand for Vertex, Weight, and Depth"""

    depth: int = field(compare=False)


def dijkstra(graph: list[list[VW]], source: V, max_depth: int) -> list[W]:
    """
    do dijkstra, within bounded depth
    """
    queue = [VWD(vertex=source, weight=0, depth=0)]
    dist: list[W] = [INF] * len(graph)

    while queue:
        cur = heappop(queue)

        if cur.depth > max_depth:
            continue

        dist[cur.vertex] = cur.weight
        for neighbor in graph[cur.vertex]:
            alt = VWD(
                vertex=neighbor.vertex,
                weight=cur.weight + neighbor.weight,
                depth=cur.depth + 1,
            )
            heappush(queue, alt)

    return dist


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # convert flights into graph
        graph: list[list[VW]] = [[] for _ in range(n)]
        for start, end, weight in flights:
            graph[start].append(VW(end, weight))

        # k is the number of stops, not all nodes!
        distances = dijkstra(graph, src, k + 1)

        if dst in distances:
            return distances[dst]
        return -1
