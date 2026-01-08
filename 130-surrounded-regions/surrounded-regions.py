class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])

        def bfs(row, col):
            board[row][col] = "not_surrounded"
            if col > 0 and board[row][col-1] == "O":
                bfs(row, col-1)
            if row > 0 and board[row-1][col] == "O":
                bfs(row-1, col)
            if col < num_cols - 1 and board[row][col+1] == "O":
                bfs(row, col+1)
            if row < num_rows - 1 and board[row+1][col] == "O":
                bfs(row+1, col)

        if num_rows == 1 or num_cols == 1:
            return board
        else: 
            for row in range(num_rows):
                for col in (0, num_cols - 1):
                    val = board[row][col]
                    if val == "O":
                        bfs(row, col)
            for col in range(1, num_cols - 1):
                for row in (0, num_rows - 1):
                    val = board[row][col]
                    if val == "O":
                        bfs(row, col)

        for row in range(num_rows):
            for col in range(num_cols):
                board[row][col] = "O" if board[row][col] == "not_surrounded" else "X"