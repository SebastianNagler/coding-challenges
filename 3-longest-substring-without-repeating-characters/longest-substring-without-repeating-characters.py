class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_map = {}
        res = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in window_map:
                window_map[s[j]] = j
                j += 1
                res = max(res, j - i)
            else:
                while s[j] in window_map:
                    del window_map[s[i]]
                    i += 1

        return res