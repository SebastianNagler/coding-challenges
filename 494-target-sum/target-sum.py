class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if target > sum_nums or target < -sum_nums:
            return 0
        num_rows = target + sum_nums + 1
        num_cols = len(nums) + 1
        first_row = [1]
        for i in range(1, num_cols):
            first_row.append(int(first_row[-1]))
            if nums[i - 1] == 0:
                first_row[-1] *= 2
        grid = [first_row] + [[0] * num_cols for _ in range(num_rows - 1)]
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                grid[row][col] += grid[row][col - 1]
                if row - (2 * nums[col - 1]) >= 0:
                    grid[row][col] += grid[row - (2 * nums[col - 1])][col - 1]

        return grid[num_rows - 1][num_cols - 1]