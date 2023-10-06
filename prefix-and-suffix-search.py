class TrieNode:

    def __init__(self):
        self.children = defaultdict(list)
        self.val = 0

class Trie:
    
    def __init__(self):
        self.root = TrieNode()  

    def insert(self, word, index) -> None:

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
            curr.val = index

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.val  

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for index, word in enumerate(words):
            for i in range(len(word)):
                newWord = word[i:] + "{" + word
                self.trie.insert(newWord, index)

    def f(self, pref: str, suff: str) -> int:
        word = suff + "{" + pref
        return self.trie.search(word)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)