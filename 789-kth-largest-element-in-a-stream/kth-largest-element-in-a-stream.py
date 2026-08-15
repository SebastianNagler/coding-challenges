class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) == k - 1:
            heap = nums + [float("-inf")]
            heapq.heapify(heap)
            self.nums = heap
        elif len(nums) == k:
            heapq.heapify(nums)
            self.nums = nums
        else:
            heap = nums[0:k]
            heapq.heapify(heap)
            for num in nums[k:]:
                if num > heap[0]:
                    heapq.heappushpop(heap, num)
            self.nums = heap
        

    def add(self, val: int) -> int:
        if val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)