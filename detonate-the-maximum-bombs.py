class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x,y,z = bombs[i]
                    a,b,c = bombs[j]
                    distance = sqrt(((x-a)**2) + ((y-b)**2))
                    if z >= distance:
                        adjList[i].append(j)
        visited = set()
        def dfs(node):
            visited.add(node)
            count = 0
            for x in adjList[node]:
                if x not in visited:
                    count += dfs(x)
            return count + 1

        ans = 1
        keys = list(adjList.keys())
        for key in keys:
            ans = max(ans, dfs(key))
            visited = set()

        return ans