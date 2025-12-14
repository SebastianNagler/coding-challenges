class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

        

    def addNum(self, num: int) -> None:
        size_min_heap = len(self.min_heap)
        size_max_heap = len(self.max_heap)
        if size_min_heap == size_max_heap:
            if size_min_heap == 0 or num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif size_min_heap > size_max_heap:
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.max_heap, -self.min_heap[0])
                heapq.heappushpop(self.min_heap, num)
        else:
            if num > -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, -self.max_heap[0])
                heapq.heappushpop(self.max_heap, -num)
        

    def findMedian(self) -> float:
        size_min_heap = len(self.min_heap)
        size_max_heap = len(self.max_heap)
        if size_min_heap == size_max_heap:
            return (self.min_heap[0] - self.max_heap[0])/2
        elif size_min_heap < size_max_heap:
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()