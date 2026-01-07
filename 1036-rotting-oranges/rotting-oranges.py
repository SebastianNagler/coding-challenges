class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(dist, row, col):
            grid[row][col] = dist
            if col > 0 and grid[row][col-1] > dist + 1:
                bfs(dist+1, row, col-1)
            if row > 0 and grid[row-1][col] > dist + 1:
                bfs(dist+1, row-1, col)
            if col + 1 < num_cols and grid[row][col+1] > dist + 1:
                bfs(dist+1, row, col+1)
            if row + 1 < num_rows and grid[row+1][col] > dist + 1:
                bfs(dist+1, row+1, col)

        for row in range(num_rows):
            for col in range(num_cols):
                val = grid[row][col]
                match val:
                    case 0:
                        grid[row][col] = -1
                    case 1:
                        grid[row][col] = float("inf")
                    case 2:
                        grid[row][col] = 0

        for row in range(num_rows):
            for col in range(num_cols):
                val = grid[row][col]
                if val == 0:
                    bfs(0, row, col)

        max_dur = 0
        for row in range(num_rows):
            for col in range(num_cols):
                val = grid[row][col]
                max_dur = max(max_dur, val)
        
        return -1 if max_dur == float("inf") else max_dur