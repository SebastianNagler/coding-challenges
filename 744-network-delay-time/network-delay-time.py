class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: [] for node in range(1, n+1)}
        for source, target, time in times:
            graph[source].append((target, time))
        heap = [(0, k)]
        dist = [float("inf") for _ in range(n)]
        dist[k - 1] = 0
        while heap:
            popped_dist, popped_node = heapq.heappop(heap)
            if popped_dist == dist[popped_node - 1]:
                for child, weight in graph[popped_node]:
                    if popped_dist + weight < dist[child - 1]:
                        dist[child - 1] = popped_dist + weight
                        heapq.heappush(heap, (dist[child - 1], child))
        max_entry = max(dist)
        return -1 if max_entry == float("inf") else max_entry

