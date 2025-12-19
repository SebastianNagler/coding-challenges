class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(row, col):
            visited.add((row, col))
            if row > 0 and (row-1, col) not in visited and grid[row-1][col] == "1":
                dfs(row-1, col)
            if col + 1 < num_cols and (row, col+1) not in visited and grid[row][col+1] == "1":
                dfs(row, col+1)
            if row + 1 < num_rows and (row+1, col) not in visited and grid[row+1][col] == "1":
                dfs(row+1, col)
            if col > 0 and (row, col-1) not in visited and grid[row][col-1] == "1":
                dfs(row, col-1)

        for row in range(num_rows):
            for col in range(num_cols):
                val = grid[row][col]
                if val == "1" and (row, col) not in visited:
                    num_islands += 1
                    dfs(row, col)


        return num_islands