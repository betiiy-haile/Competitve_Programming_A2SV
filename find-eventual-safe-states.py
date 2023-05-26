class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0] * len(graph)
        ans = []

        def dfs(node):
            colors[node] = 1

            for child in graph[node]:
                if colors[child] == 2:
                    continue
                elif colors[child] == 1:
                    return False
                else:
                    if not dfs(child):
                        return False
            ans.append(node)
            colors[node] = 2
            return True

        for node in range(len(graph)):
            if colors[node] == 0:
                dfs(node)

        ans.sort()
        return ans