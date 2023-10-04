class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root=TrieNode() 

    def insert(self, word):
        curr = self.root

        for char in word:            
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
        curr.isEnd = True    

    def startsWith(self, prefix):
        curr = self.root

        for char in prefix:            
            if curr.children[char].isEnd == False:
                return False
            
            curr = curr.children[char]
        
        return True 

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        ans = ""

        for word in words:
            if trie.startsWith(word):
                if len(ans) < len(word):
                    ans = word
                elif len(ans) == len(word) and word < ans:
                    ans = word
        
        return ans