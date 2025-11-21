class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        indices = []
        if len_s < len_p:
            return indices
        p_counter = Counter(p)
        for i in range(len_s - len_p + 1):
            if s[i] in p_counter:
                if Counter(s[i:i + len_p]) == p_counter:
                    indices.append(i)
        return indices