class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = {'(', '[', '{'}
        mapping = {')': '(', ']': '[', '}': '{'}
        open_stack = deque()
        for char in s:
            if char in open_chars:
                open_stack.append(char)
            else:
                if open_stack and mapping[char] == open_stack.pop():
                    pass
                else:
                    return False
        if open_stack:
            return False
        return True
