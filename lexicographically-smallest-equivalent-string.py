class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i + 97) : chr(i + 97) for i in range(26)}
        
        def find(node):
            if parent[node] == node:
                return node
            grandParent = find(parent[node])
            parent[node] = grandParent
            return grandParent

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return
            if ord(parent1) < ord(parent2):
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2
        
        for i in range(len(s1)):
            union(s1[i], s2[i])

        ans = ''
        for i in baseStr:
            ans += find(i)
        return ans