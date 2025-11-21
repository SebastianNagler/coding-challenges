class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        len_s = len(s)
        len_t = len(t)
        len_t_counter = len(t_counter)
        left = 0
        s_counter = Counter('')
        min_length = float('inf')
        solution_index = 0
        num_insuff_chars = len_t_counter

        for right in range(len_s):
            right_char = s[right]
            if right_char in s_counter:
                s_counter[right_char] += 1
            else:
                s_counter[right_char] = 1
            if s_counter[right_char] == t_counter[right_char]:
                num_insuff_chars -= 1
            while num_insuff_chars == 0:
                len_substr = right - left + 1
                if len_substr < min_length:
                    solution_index = left
                    min_length = len_substr
                left_char = s[left]
                if s_counter[left_char] == t_counter[left_char]:
                    num_insuff_chars += 1
                s_counter[s[left]] -= 1
                left += 1
            
        return '' if min_length == float('inf') else s[solution_index:solution_index + min_length]
            
