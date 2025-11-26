class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        left, right = 0, num_rows * num_cols - 1
        while left <= right:
            mid = (left + right) // 2
            row, column = divmod(mid, num_cols)
            val = matrix[row][column]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False