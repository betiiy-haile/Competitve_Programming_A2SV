class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)

        count = 0
        visited = set()
        def dfs(graph, source):
            visited.add(source)
            for x in graph[source]:
                if x not in visited:
                    dfs(graph, x)

        for i in range(len(isConnected)):
            if i+1 not in visited:
                count += 1
                dfs(graph, i+1)

        return count