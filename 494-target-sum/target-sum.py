class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if target > sum(nums) or target < -sum(nums):
            return 0
        num_rows = target + sum(nums) + 1
        num_cols = len(nums) + 1
        grid = [[1]] + ([[0] for i in range(num_rows - 1)])
        for i in range(1, num_cols):
            grid[0].append(int(grid[0][-1]))
            if nums[i - 1] == 0:
                grid[0][-1] *= 2
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                grid[row].append(0)
                grid[row][col] += grid[row][col - 1]
                if row - (2 * nums[col - 1]) >= 0:
                    grid[row][col] += grid[row - (2 * nums[col - 1])][col - 1]

        return grid[num_rows - 1][num_cols - 1]