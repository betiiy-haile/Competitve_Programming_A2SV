class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        incoming = [0] * len(edges)

        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
                incoming[edges[i]] += 1

        visited = set()
        maxLen = -1

        def dfs(node):
            nonlocal maxLen
            if node in visited:
                return [node, 1]

            curr = [-1,-1]
            visited.add(node)

            for child in graph[node]:
                temp = dfs(child)
                if curr[1] < temp[1]:
                    curr = temp

            if curr[0] == node:
                maxLen = max(maxLen,curr[1])
            else:
                curr[1] += 1

            return curr

        for i in range(len(edges)):
            if i not in visited:
                dfs(i)

        return maxLen