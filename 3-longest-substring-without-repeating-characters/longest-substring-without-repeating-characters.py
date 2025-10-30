class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        local_chars = {s[0]: 1}
        i = 0
        j = 1
        max_length = 0
        while j <= len(s):
            num_chars = j - i
            num_unique_chars = len(local_chars)
            if num_unique_chars < num_chars:
                if local_chars[s[i]] == 1:
                    del local_chars[s[i]]
                else:
                    local_chars[s[i]] -= 1
                i += 1
            elif num_chars > max_length:
                max_length = num_chars
            else:
                if j < len(s):
                    if s[j] in local_chars:
                        local_chars[s[j]] += 1
                    else:
                        local_chars[s[j]] = 1
                j += 1
        return max_length


