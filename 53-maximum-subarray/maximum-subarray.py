class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num < 0:
            return max_num
        max_sum = 0
        curr_sum = 0
        active = False
        for i in range(len(nums)):
            if active:
                curr_sum += nums[i]
                if curr_sum < 0:
                    active = False
                    continue
                max_sum = max(max_sum, curr_sum)
            else:
                if nums[i] > 0:
                    active = True
                    curr_sum = nums[i]
                    max_sum = max(max_sum, nums[i])

        return max_sum