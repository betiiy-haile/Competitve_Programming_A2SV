class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)
        self.isEnd = False   
        self.count = 0 

class Trie:
    def __init__(self):
        self.root = TrieNode()  

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word: 
            if char not in curr.children:
                curr.children[char] = TrieNode()                
            curr = curr.children[char]
            curr.count += 1 
        curr.isEnd = True
         

    def search(self, word: str) -> bool:
        val = 0
        curr = self.root
        for char in word:
            curr = curr.children[char]
            val += curr.count

        return val

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        ans = []
        for word in words:
            trie.insert(word)            

        for word in words:
            val = trie.search(word)
            ans.append(val)
        return ans