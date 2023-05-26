"""https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
from dataclasses import dataclass, field
from heapq import heappush, heappop


V = int  # vertex id
W = int  # weight


@dataclass(order=True)
class VW:
    """shorthand for Vertex and Weight"""

    vertex: int = field(compare=False)
    weight: int


@dataclass(order=True)
class VWD(VW):
    """shorthand for Vertex, Weight, and Depth"""

    depth: int = field(compare=False)


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """Dijkstra 정신을 활용한 문제풀이. K-stop 이내에 dst에 도착하는 최소거리

        Args:
            n : number of vertices
            flights : given graphs, [src, dst, weight]
            k : within k-stops to arrive

        Returns:
            int: _description_
        """
        # convert flights into graph
        graph: list[list[VW]] = [[] for _ in range(n)]
        for start, end, weight in flights:
            graph[start].append(VW(end, weight))

        queue = [VWD(vertex=src, weight=0, depth=0)]

        while queue:
            cur = heappop(queue)
            if cur.vertex == dst:
                return cur.weight
            # 1순위: 경유지 count (depth)
            if cur.depth > k:
                continue
            # 2순위: min weight -- 왜 아저씨 코드에는 minimum 계산이 없지?
            for neighbor in graph[cur.vertex]:
                alt = VWD(
                    vertex=neighbor.vertex,
                    weight=cur.weight + neighbor.weight,
                    depth=cur.depth + 1,
                )
                heappush(queue, alt)

        return -1
