class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        desired_sum = int(sum_nums / 2)
        dp = [True]
        for i in range(desired_sum):
            dp.append(False)
        for num in nums:
            for i in range(desired_sum, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[-1]