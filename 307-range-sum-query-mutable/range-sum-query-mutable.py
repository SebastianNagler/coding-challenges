class NumArray:        
    def __init__(self, nums: List[int]):
        self.len = len(nums)
        self.size = 1 << (self.len - 1).bit_length()
        self.nums = [0] * 2 * self.size
        self.nums[self.size:self.size + self.len] = nums
        for i in range(self.size - 1, 0, -1):
            self.nums[i] = self.nums[2 * i] + self.nums[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        index += self.size
        self.nums[index] = val
        index >>= 1
        while index > 0:
            self.nums[index] = self.nums[2 * index] + self.nums[2 * index + 1]
            index >>= 1

    def sumRange(self, left: int, right: int) -> int:
        left, right = left + self.size, right + self.size + 1
        left_curr, right_curr = 0, 0
        while left < right:
            if left & 1:
                left_curr = left_curr + self.nums[left]
                left += 1
            if right & 1:
                right -= 1
                right_curr = right_curr + self.nums[right]
            left >>= 1
            right >>= 1

        return left_curr + right_curr

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)