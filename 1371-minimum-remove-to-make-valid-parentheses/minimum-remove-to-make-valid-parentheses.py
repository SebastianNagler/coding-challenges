class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_available = 0
        closed_available = 0
        res = []
        for char in s:
            if char == ')':
                closed_available += 1
        for char in s:
            if char.isalpha():
                res.append(char)
            elif char == '(':
                if closed_available:
                    closed_available -= 1
                    open_available += 1
                    res.append(char)
            else:
                if open_available:
                    open_available -= 1
                    res.append(char)
                else:
                    closed_available -= 1
        return res