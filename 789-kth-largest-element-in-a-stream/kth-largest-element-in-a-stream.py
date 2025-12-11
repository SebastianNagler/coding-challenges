class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.missing = len(nums) < k
        self.heap = nums[:k] if not self.missing else nums[:k-1]
        heapq.heapify(self.heap)
        for elem in nums[k:]:
            if elem > self.heap[0]:
                heapq.heappushpop(self.heap, elem)

    def add(self, val: int) -> int:
        if self.missing:
            heapq.heappush(self.heap, val)
            self.missing = False
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)