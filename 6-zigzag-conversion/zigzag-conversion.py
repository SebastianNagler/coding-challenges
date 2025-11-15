class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for i in range(numRows)]
        num_chars = 2 * numRows - 2

        for i in range(len(s)):
            mod_result = i % num_chars
            if mod_result < numRows:
                rows[mod_result] += s[i]
            else:
                row_index = numRows - (mod_result - numRows) - 2
                rows[row_index] += s[i]

        rows_concatenation = str()
        for row in rows:
            rows_concatenation += row
        return rows_concatenation