class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = { chr(i+97) : chr(i+97) for i in range(26)}

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

            parent[parent2] = parent1

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])

        for eq in equations:
            if (eq[1] == "!" and find(eq[0]) == find(eq[3])):
                return False
        return True