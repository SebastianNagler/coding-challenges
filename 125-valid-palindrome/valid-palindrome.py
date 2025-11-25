class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''
        for char in s:
            if (char.isalpha() or char.isdigit()) and char != ' ':
                cleaned_str += char.lower()
        i = 0
        j = len(cleaned_str) - 1
        while i < j:
            if cleaned_str[i] != cleaned_str[j]:
                return False
            i += 1
            j -= 1
        return True