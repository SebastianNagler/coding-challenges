class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        len_s = len(s)
        len_t = len(t)
        left = 0
        s_counter = Counter('')
        min_length = float('inf')
        solution = ''

        for right in range(len_s):
            right_char = s[right]
            if right_char in s_counter:
                s_counter[right_char] += 1
            else:
                s_counter[right_char] = 1
            while t_counter <= s_counter:
                len_substr = right - left + 1
                if len_substr < min_length:
                    solution = s[left:right + 1]
                    min_length = len_substr
                s_counter[s[left]] -= 1
                left += 1
        return solution
            
