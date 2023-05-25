"""
https://leetcode.com/problems/network-delay-time/
min heap을 활용한 다익스트라
"""
import collections
import heapq


V = int  # Vertex
W = int  # Weight


def dijkstra(graph: list[list[tuple[V, W]]], source: V) -> dict[V, W]:
    """
    source로부터 graph 안의 모든 노드들 사이에 최단거리를 리턴한다.
    만약 닿을 수 없는 노드라면 key 값에 포함이 되어있지 않는 식으로 처리했다.
    """

    # source로부터 v까지 필요한 거리
    # 위키와 다른 형태 주의
    queue: list[tuple[V, W]] = [(source, 0)]
    # source에서 v까지 최단거리
    # 위키와 다른 형태 주의. INF 값을 사용하지 않고 그냥 dict를 비워두는 것.
    dist: dict[V, W] = collections.defaultdict(W)

    while queue:
        # 가장 가까운 노드부터 꺼낸다. -- 위키피디아의 것과 일치
        vertex, weight = heapq.heappop(queue)

        if vertex in dist:
            # 해당 버텍스로 가는 최단거리가 이미 구해졌다.
            # 따라서 해당값을 그냥 버린다.
            continue

        # vertex까지 가는 최단거리를 찾았다.
        dist[vertex] = weight

        for n_vertex, n_weight in graph[vertex]:
            # vertex와 인접한 노드들을 순회
            # 이때 source로부터 vertex까지의 최단거리인 weight를
            # 추가해 주어야 한다는 것이다.
            alt = n_weight + weight
            heapq.heappush(queue, (n_vertex, alt))

    return dist


class Solution:

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        return the minimum time it takes for all the n nodes to receive the
        signal. If it is impossible, return -1

        params:
        - times: list of [u, v, w], where u is the source node, v is the
            target node, w is the time it takes for a signal to travel
            from source to target.
        - n: number of nodes
        - k: very first node that tries to send signal
        """
        # normalise indices
        times = [[u-1, v-1, w] for u, v, w in times]
        k = k - 1

        # create a graph
        graph = [[] for _ in range(n)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = dijkstra(graph, k)

        if len(dist) != n:
            return -1
        return max(dist.values())
