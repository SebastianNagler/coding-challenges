from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices_list = []
        words_dict = Counter(words)
        len_word = len(words[0])
        len_words = len(words)
        len_con_str = len_word * len_words
        len_s = len(s)
        for i in range(len_s):
            if len_s - i >= len_con_str:
                local_words = defaultdict(int)
                for j in range(len_words):
                    local_words[s[i + (j * len_word):i + ((j + 1) * len_word)]] += 1
                if local_words == words_dict:
                    indices_list.append(i)
        return indices_list                                                                               

