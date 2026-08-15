class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split()
        l = [l[-i-1] for i in range(len(l))]
        return " ".join(l)