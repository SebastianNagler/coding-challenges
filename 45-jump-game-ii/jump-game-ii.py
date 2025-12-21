class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        num_jumps = 1
        low = 1
        high = nums[0]
        while high < n - 1:
            num_jumps += 1
            local_max = float("-inf")
            for idx in range(low, high + 1):
                local_max = max(local_max, idx + nums[idx])
            low = high + 1
            high = local_max

        return num_jumps