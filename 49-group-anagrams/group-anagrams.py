class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        strs_map = {}
        res = []
        for s in strs:
            tup_rep = tuple(sorted(s))
            if tup_rep in strs_map:
                res[strs_map[tup_rep]].append(s)
            else:
                strs_map[tup_rep] = i
                i += 1
                res.append([s])

        return res