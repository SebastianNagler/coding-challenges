class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums > 2:
            nums[2] += nums[0]
        for i in range(3, len_nums):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[len_nums - 1], nums[len_nums - 2])