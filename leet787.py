"""https://leetcode.com/problems/cheapest-flights-within-k-stops/
notice: 책에 있는 코드로는 더 이상 ACCEPT가 나오지 않는다. 다음 링크를 참조하여 더 효율적인 코드에 대한 토론을 확인해보자.
    https://github.com/onlybooks/algorithm-interview/issues/104
"""
from collections import defaultdict
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
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # queue = [(weight, vertex, depth)]
        queue = [(0, src, 0)]

        while queue:
            cur_w, cur_v, cur_k = heappop(queue)
            if cur_v == dst:
                return cur_w
            if cur_k > k:
                continue
            # iterate neighbors
            for neigh_v, neigh_w in graph[cur_v]:
                alt_w = neigh_w + cur_w
                alt_k = cur_k + 1
                heappush(queue, (alt_w, neigh_v, alt_k))
        return -1
