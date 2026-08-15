class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).lower()
        word_counter = Counter(paragraph.split())
        for s in banned:
            if s in word_counter:
                del word_counter[s]
        return word_counter.most_common(1)[0][0]