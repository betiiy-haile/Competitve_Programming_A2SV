class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        def dfs(node):
            time = 0
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    childTime = dfs(child)
                    if childTime or hasApple[child]:
                        time += 2 + childTime
            return time

        return dfs(0)