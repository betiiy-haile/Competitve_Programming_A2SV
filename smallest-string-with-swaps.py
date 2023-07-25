class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        parent = list(range(len(s)))

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
            parent[parent1] = parent2

        for x, y in pairs:
            union(x, y)

        IndexGroup = defaultdict(list) 
        CharGroup = defaultdict(list)

        for i in range(len(s)):
            group = find(i) 
            IndexGroup[group].append(i)
            CharGroup[group].append(s[i]) 

        res = [""] * len(s)
        for group in IndexGroup.keys():
            index = sorted(IndexGroup[group])
            chars = sorted(CharGroup[group])
            for i, c in zip(index, chars):
                res[i] = c

        return "".join(res)