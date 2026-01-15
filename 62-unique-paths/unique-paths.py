class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        column = [1] * n
        grid = [column] * m
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                grid[row][col] = grid[row + 1][col] + grid[row][col + 1]
        return grid[0][0]