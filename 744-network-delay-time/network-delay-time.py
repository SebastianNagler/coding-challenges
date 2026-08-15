class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        graph = [[] for i in range(n)]
        dist = [float("inf")] * n
        dist[k] = 0
        for triple in times:
            graph[triple[0] - 1].append((triple[1] - 1, triple[2]))

        heap = [(0, k)]

        nr = 0

        seen = set()

        while heap:
            pop_dist, pop_idx = heapq.heappop(heap)
            if pop_dist == dist[pop_idx]:
                if pop_idx in seen:
                    continue
                seen.add(pop_idx)
                nr += 1
                for out_idx, out_w in graph[pop_idx]:
                    out_dist = pop_dist + out_w
                    if out_dist < dist[out_idx]:
                        dist[out_idx] = out_dist
                        heapq.heappush(heap, (out_dist, out_idx))

        if nr != n:
            return -1
        return max(dist)
