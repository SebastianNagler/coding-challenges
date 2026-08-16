class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        new_s = []
        for char in s:
            if not new_s or not (new_s[-1] == '(' and char == ')'):
                new_s.append(char)
            else:
                new_s.pop()
        return len(new_s)