class Solution:
    def countSubstrings(self, s: str) -> int:
        num_substr = len(s)
        for i in range(len(s)):
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                num_substr += 1
                low -= 1
                high += 1
            low = i
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                num_substr += 1
                low -= 1
                high += 1
                
        return num_substr