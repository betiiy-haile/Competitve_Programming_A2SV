class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {i : i for i in range(n)}
        size = [1] * n

        def find(node):
            if parent[node] == node:
                return node
            Parent = find(parent[node])
            parent[node] = Parent
            return Parent

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


        for From , To in edges:
            union(From, To)

        return find(source) == find(destination)