class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_max_idx = {}
        for i in range(len(s)):
            char_to_max_idx[s[i]] = i
        i = 0
        res = []
        while i < len(s):
            partition_start = i
            curr_end_low_bound = char_to_max_idx[s[i]]
            while i < curr_end_low_bound:
                i = i + 1
                curr_end_low_bound = max(curr_end_low_bound, char_to_max_idx[s[i]])
            i = i + 1
            res.append(i - partition_start)

        return res