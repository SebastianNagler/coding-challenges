class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            match s[i]:
                case 'I':
                    if i+1 < len(s) and s[i+1] in ('V', 'X'):
                        num -= 1
                    else:
                        num += 1
                case 'X':
                    if i+1 < len(s) and s[i+1] in ('L', 'C'):
                        num -= 10
                    else:
                        num += 10
                case 'C':
                    if i+1 < len(s) and s[i+1] in ('D', 'M'):
                        num -= 100
                    else:
                        num += 100
                case 'V':
                    num += 5
                case 'L':
                    num += 50
                case 'D':
                    num += 500
                case 'M':
                    num += 1000
        return num