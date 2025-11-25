class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            i_char = s[i].lower()
            if i_char == ' ' or not (i_char.isalpha() or i_char.isdigit()):
                i += 1
                continue
            j_char = s[j].lower()
            if j_char == ' ' or not (j_char.isalpha() or j_char.isdigit()):
                j -= 1
                continue
            if i_char != j_char:
                return False
            i += 1
            j -= 1
        return True