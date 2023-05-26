"""https://leetcode.com/problems/cheapest-flights-within-k-stops/
notice: 책에 있는 코드로는 더 이상 ACCEPT가 나오지 않는다. 다음 링크를 참조하여 더 효율적인 코드에 대한 토론을 확인해보자.
    https://github.com/onlybooks/algorithm-interview/issues/104
"""
from dataclasses import dataclass, field
from heapq import heappush, heappop


V = int  # vertex id
W = int  # weight
D = int  # depth

INF = 1 << 30


@dataclass(order=True)
class VW:
    """shorthand for Vertex and Weight"""

    vertex: V = field(compare=False)
    weight: W


@dataclass
class WD:
    """shorthand for Weight and Depth"""

    weight: W
    depth: D


@dataclass(order=True)
class VWD(VW):
    """shorthand for Vertex, Weight, and Depth"""

    depth: D = field(compare=False)


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # init graph aka adjacancy list
        graph: list[list[VW]] = [[] for _ in range(n)]
        for start, end, weight in flights:
            graph[start].append(VW(end, weight))

        # dist: 해당 노드를 방문했던 경로의 weight와 depth를 저장.
        # 이때, depth가 작은 것을 우선한다.
        dist: list[WD] = [WD(INF, 0)] * n

        queue = [VWD(src, 0, 0)]

        while queue:
            cur = heappop(queue)
            if cur.vertex == dst:
                return cur.weight
            if cur.depth > k:
                continue

            for neighbor in graph[cur.vertex]:
                # Ok, let's check we can push neighbors into the queue!
                alt_weight = neighbor.weight + cur.weight
                alt_depth = cur.depth + 1
                if (
                    alt_weight < dist[neighbor.vertex].weight
                    or alt_depth <= dist[neighbor.vertex].depth
                ):
                    dist[neighbor.vertex] = WD(alt_weight, alt_depth)
                    heappush(
                        queue, VWD(neighbor.vertex, alt_weight, alt_depth)
                    )
        return -1
