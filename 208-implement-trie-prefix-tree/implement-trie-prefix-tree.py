class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr_dict = self.root
        for char in word:
            curr_dict = curr_dict.setdefault(char, {})
        curr_dict["end"] = True

    def search(self, word: str) -> bool:
        curr_dict = self.root
        for char in word:
            if char not in curr_dict:
                return False
            curr_dict = curr_dict[char]
        return "end" in curr_dict
        

    def startsWith(self, prefix: str) -> bool:
        curr_dict = self.root
        for char in prefix:
            if char not in curr_dict:
                return False
            curr_dict = curr_dict[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)