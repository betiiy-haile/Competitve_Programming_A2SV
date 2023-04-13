class ThroneInheritance:

    def __init__(self, kingName: str):
        self.succession = []
        self.kingName = kingName
        self.adjList = defaultdict(list)
        self.deads = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.adjList[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.dfs(self.kingName)
        self.ans = self.succession
        self.succession = []
        return self.ans

    def dfs(self, node):
        if node not in self.deads:
            self.succession.append(node)
        for child in self.adjList[node]:
            self.dfs(child)

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()