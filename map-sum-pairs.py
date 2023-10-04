class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode() 
        self.words= {}    
        
    def insert(self, key: str, val: int) -> None:
        num = val
        if key in self.words:
            num -= self.words[key]
        self.words[key] = val
            
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr.children[char].count += num
            curr = curr.children[char]

        curr.isEnd = True


    def sum(self, prefix: str) -> int:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]

        return curr.count
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)