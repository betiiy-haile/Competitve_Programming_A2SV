class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i+1 : i+1 for i in range(len(edges) + 1)}
        size = [1] * (len(edges) + 1)

        def find(node):
            if parent[node] == node:
                return parent[node] 
            grandParent = find(parent[node])
            parent[node] = grandParent
            return grandParent

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return
            if size[parent1] > size[parent2]:
                parent[parent2] = parent1
                size[parent2] += size[parent1]
            else:
                parent[parent1] = parent2
                size[parent1] += size[parent2]
        ans = []
        for From , To in edges:
            if find(From) == find(To):
                ans = [From, To]
            union(From, To)

        return ans