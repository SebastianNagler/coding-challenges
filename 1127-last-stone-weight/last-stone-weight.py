class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-elem for elem in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x - y)
        if len(heap) == 1:
            return -heap[0]
        return 0