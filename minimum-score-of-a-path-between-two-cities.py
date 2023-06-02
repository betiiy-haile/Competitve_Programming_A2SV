class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = { i : i for i in range(1, n + 1)} 
        size = [1] * (n + 1)
        connected = set()

        def find(node):
            if node == parent[node]:
                return node
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
        
        for node1, node2, dis in roads:
            union(node1, node2) 

        for k, v in parent.items():
            if find(v) == find(1):
                connected.add(k)

        min = float('inf')
        for node1, node2, dis in roads:
            if (node1 in connected or node2 in connected) and dis < min:
                min = dis

        return min