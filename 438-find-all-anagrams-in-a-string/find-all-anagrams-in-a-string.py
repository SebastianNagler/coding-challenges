class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        indices = []
        if len_s < len_p:
            return indices
        p_counter = Counter(p)
        s_counter = Counter(s[0:len_p - 1])
        for i in range(len_s - len_p + 1):
            if i != 0:
                s_counter[s[i - 1]] -= 1
            if s[i + len_p - 1] in s_counter:
                s_counter[s[i + len_p - 1]] += 1
            else:
                s_counter[s[i + len_p - 1]] = 1
            if s[i] in p_counter:
                if s_counter == p_counter:
                    indices.append(i)
        return indices