class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        s1_c, s2_substr_c = Counter(s1), Counter(s2[:len1])
        left, right = 0, len1 - 1
        if len2 < len1:
            return False
        while right < len2:
            if s2_substr_c == s1_c:
                return True
            left += 1
            right += 1
            if right < len2:
                s2_substr_c[s2[left-1]] -= 1
                s2_substr_c[s2[right]] = s2_substr_c.get(s2[right], 0) + 1

        return False