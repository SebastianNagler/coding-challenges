class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rule 1: Each row must contain the digits 1-9 without repetition.
        for row in board:
            row_numbers_set = set()
            for entry in row:
                if entry.isdigit():
                    if entry in row_numbers_set:
                        return False
                    row_numbers_set.add(entry)

        # Rule 2: Each column must contain the digits 1-9 without repetition.
        for column_index in range(9):
            column_numbers_set = set()
            for row_index in range(9):
                entry = board[row_index][column_index]
                if entry.isdigit():
                    if entry in column_numbers_set:
                        return False
                    column_numbers_set.add(entry)

        # Rule 3: Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for large_row_index in range(3):
            for large_column_index in range(3):
                square_numbers_set = set()
                for row_index in range(3 * large_row_index, 3 * (large_row_index + 1)):
                    for column_index in range(3 * large_column_index, 3 * (large_column_index + 1)):
                        entry = board[row_index][column_index]
                        if entry.isdigit():
                            if entry in square_numbers_set:
                                return False
                            square_numbers_set.add(entry)
        return True