class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        right = 0
        sum = nums[0]

        for left in range(len(nums)):
            while sum < target:
                if right == len(nums) - 1:
                    return 0 if min_length == float('inf') else min_length
                right += 1
                sum += nums[right]
            min_length = min(min_length, right - left + 1)
            sum -= nums[left]

        return 0 if min_length == float('inf') else min_length