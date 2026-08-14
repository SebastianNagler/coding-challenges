class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(s) for s in strs]
        min_len = min(lengths)
        for i in range(min_len):
            char = strs[0][i]
            if any([char != s[i] for s in strs]):
                return strs[0][0:i]
        return strs[0][0:min_len]