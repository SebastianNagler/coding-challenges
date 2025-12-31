class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        max_area = 0
        local_area = 0

        def bfs(row: int, col: int) -> None:
            nonlocal local_area
            local_area += 1
            grid[row][col] = -1
            if col > 0 and grid[row][col-1] == 1:
                bfs(row, col-1)
            if row > 0 and grid[row-1][col] == 1:
                bfs(row-1, col)
            if col < num_cols - 1 and grid[row][col+1] == 1:
                bfs(row, col+1)
            if row < num_rows - 1 and grid[row+1][col] == 1:
                bfs(row+1, col)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    bfs(row, col)
                    max_area = max(max_area, local_area)
                    local_area = 0

        return max_area
