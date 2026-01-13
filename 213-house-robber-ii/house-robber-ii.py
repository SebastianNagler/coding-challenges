class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        outer_nums = nums[:len(nums) - 1]
        inner_nums = nums[1:len(nums) - 2][:]
        outer_nums[2] += outer_nums[0]
        if len(inner_nums) > 2:
            inner_nums[2] += inner_nums[0]
        for i in range(3, len(outer_nums)):
            outer_nums[i] += max(outer_nums[i-2], outer_nums[i-3])
        for i in range(3, len(inner_nums)):
            inner_nums[i] += max(inner_nums[i-2], inner_nums[i-3])

        outer_max = max(outer_nums[-1], outer_nums[-2])
        inner_max = inner_nums[0]
        if len(inner_nums) > 1:
            inner_max = max(inner_nums[-1], inner_nums[-2])
        return max(outer_max, inner_max + nums[-1])