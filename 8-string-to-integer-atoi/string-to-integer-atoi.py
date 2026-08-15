class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        is_neg = False
        if s[0] == "-":
            is_neg = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        if not s:
            return 0
        if not s[0].isdigit():
            return 0
        i = 0
        for char in s:
            if char.isdigit():
                i += 1
            else:
                break
        val = 0
        for j in range(0, i):
            val += int(s[i-j-1]) * (10 ** j)
        if is_neg:
            val = -val
        if val < - 2**31:
            val = -2**31
        elif val > 2**31 - 1:
            val = 2**31 - 1
        return val