class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == '' or text2 == '':
            return 0
        num_rows, num_cols = len(text1), len(text2)
        matrix = [[0] * (num_cols + 1) for n in range(num_rows + 1)]
        for row in range(1, num_rows + 1):
            for col in range(1, num_cols + 1):
                if text1[row-1] == text2[col-1]:
                    matrix[row][col] = matrix[row-1][col-1] + 1
                else:
                    matrix[row][col] = max(matrix[row-1][col-1], matrix[row][col-1], matrix[row-1][col])
        return matrix[num_rows][num_cols]