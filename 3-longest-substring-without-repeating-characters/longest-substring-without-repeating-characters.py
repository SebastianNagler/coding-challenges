class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        local_chars = set()
        i = 0
        j = 1
        max_length = 0
        while j <= len(s):
            num_chars = len(s[i:j])
            num_unique_chars = len(set(s[i:j]))
            if num_unique_chars < num_chars:
                i += 1
            elif num_chars > max_length:
                max_length = num_chars
            else:
                j += 1
        return max_length


