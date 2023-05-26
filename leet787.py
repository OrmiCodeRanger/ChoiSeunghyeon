"""https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, TypeVar, Generic
from heapq import heappush, heappop


T = TypeVar("T")
V = int  # vertex id
W = int  # weight


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


def dijkstra(
    graph: list[list[VW]], source: V, max_depth: int
) -> tuple[dict[V, W], list[V]]:
    """do basic dijkstra but with an additional predicate"""

    # queue = [vertex, weight, depth]
    queue = [VWD(source, 0, 0)]

    dist: dict[V, W] = defaultdict(W)

    # prev stores previous vertex
    prev: list[V] = [source for _ in range(len(graph))]

    while queue:
        cur = heappop(queue)
        if cur.depth > max_depth:
            continue

        if cur.vertex not in dist or cur.weight <= dist[cur.vertex]:
            # Ok, we finally have the shortest path from src to cur
            dist[cur.vertex] = cur.weight

        for neighbor in graph[cur.vertex]:
            # we MUST add additional weight to get through to the neighbor
            alt = VWD(
                neighbor.vertex, neighbor.weight + cur.weight, cur.depth + 1
            )
            heappush(queue, alt)
            prev[neighbor.vertex] = cur.vertex

    return (dist, prev)


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # convert flights into graph
        graph: list[list[VW]] = [[] for _ in range(n)]
        for start, end, weight in flights:
            graph[start].append(VW(end, weight))

        # k is the number of stops, not all nodes!
        distances, prev = dijkstra(graph, src, k + 1)

        if dst in distances:
            return distances[dst]
        return -1
