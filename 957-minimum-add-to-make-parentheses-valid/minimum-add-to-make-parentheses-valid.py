class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closed_prefix = 0
        open_suffix = 0
        for char in s:
            if char == '(':
                open_suffix += 1
            else:
                if open_suffix > 0:
                    open_suffix -= 1
                else:
                    closed_prefix += 1
        return closed_prefix + open_suffix