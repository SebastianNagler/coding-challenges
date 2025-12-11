class WordDictionary:

    def __init__(self):
        self.root = {}
        
    def addWord(self, word: str) -> None:
        curr_dict = self.root
        for char in word:
            curr_dict = curr_dict.setdefault(char, {})
        curr_dict['end'] = True

    def search(self, word: str) -> bool:
        
        def recursiveSearch(word, node):
            i = 1
            for char in word:
                if char == '.':
                    for k in node:
                        if recursiveSearch(k + word[i:], node):
                            return True
                    return False
                elif char not in node:
                    return False
                else:
                    node = node[char]
                i += 1
            return 'end' in node

        return recursiveSearch(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)