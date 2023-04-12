class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        color = [0]*(n+1)
        visited = set()    
        def dfs(node, c):
            if node in visited:
                if color[node] != c:
                    return False
                return True

            color[node] = c
            visited.add(node)

            for nxtNode in graph[node]:
                if not dfs(nxtNode, -c):
                    return False
            return True

        for i in range(len(graph)):
            if not color[i]:
                if not dfs(i,1):
                    return False
        return True