class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        min_len = min([len(s) for s in strs])
        if strs == []:
            return ''
        while True:
            if i == min_len:
                return strs[0][0:i]
            elif all(s[i] == strs[0][i] for s in strs):
                i += 1
            else:
                return strs[0][0:i]