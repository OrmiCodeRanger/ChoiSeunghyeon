"""https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
from dataclasses import dataclass, field
from typing import Any, TypeVar, Generic
from heapq import heappush, heappop
from collections import defaultdict


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


def dijkstra(
    graph: list[list[VW]], source: V, predicate
) -> tuple[dict[V, W], list[V]]:
    """do basic dijkstra but with an additional predicate"""

    # always be zero-weight to myself
    queue = [VW(source, 0)]
    # stores minimum distance between source and each vertices,
    # note that if vertex cannot approach, `dist` won't store any entry.
    dist: dict[V, W] = {}
    # prev stores previous vertex
    prev: list[V] = [source for _ in range(len(graph))]

    while queue:
        cur = heappop(queue)
        if not predicate(prev, cur.vertex) or cur.vertex in dist:
            # additional business logic for extensibility
            # already have a shortest dist to cur!!!
            continue
        # Ok, we finally have the shortest path from src to cur
        dist[cur.vertex] = cur.weight
        for neighbor in graph[cur.vertex]:
            # we MUST add additional weight to get through to the neighbor
            alt = VW(neighbor.vertex, neighbor.weight + cur.weight)
            heappush(queue, alt)
            prev[neighbor.vertex] = cur.vertex

    return (dist, prev)


def counter(max_count=0):
    """create a closure"""

    def wrap(prev, vertex) -> bool:
        cnt = 0
        cur = vertex
        while cur != prev[cur]:
            cur = prev[cur]
            cnt += 1
        return cnt <= max_count

    return wrap


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # convert flights into graph
        graph: list[list[VW]] = [[] for _ in range(n)]
        for src, dst, weight in flights:
            graph[src].append(VW(dst, weight))

        # k is the number of stops, not all nodes!
        distances, prev = dijkstra(graph, src, counter(k + 1))

        if dst in distances:
            return distances[dst]
        return -1
