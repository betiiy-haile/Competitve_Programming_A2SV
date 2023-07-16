class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = { (x, y ): (x, y) for (x, y) in stones}
        rank = { (x, y ): 0 for (x, y) in stones}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                rank[py] += 1

        connected = set()
        for i in range(len(stones)):
            for j in range(len(stones)):
                stone1 = stones[i]
                stone2 = stones[j]
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    union((stone1[0], stone1[1]), (stone2[0], stone2[1]))
        
        for x, y in stones:
            connected.add(find((x, y)))
        return len(stones) - len(connected)