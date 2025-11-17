class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_zeros = set()
        cols_with_zeros = set()
        matrix_shape = (len(matrix), len(matrix[0]))
        for row_index in range(matrix_shape[0]):
            for col_index in range(matrix_shape[1]):
                if matrix[row_index][col_index] == 0:
                    rows_with_zeros.add(row_index)
                    cols_with_zeros.add(col_index)

        zeroes_row = [0 for i in range(matrix_shape[1])]
        for r in rows_with_zeros:
            matrix[r] = zeroes_row

        for c in cols_with_zeros:
            for row_index in range(matrix_shape[0]):
                matrix[row_index][c] = 0
        return matrix