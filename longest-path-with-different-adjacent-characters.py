class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjList = defaultdict(list)
        for idx, par in enumerate(parent):
            if par >= 0:
                adjList[par].append(idx)  

        ans = 1
        def dfs(node):
            nonlocal ans
            maxChilds = [0, 0]

            for child in adjList[node]:
                maxPath = dfs(child)
                if s[child] != s[node]:
                    maxChilds.append(maxPath)
                    maxChilds = sorted(maxChilds, reverse=True)[:2] 

            ans = max(ans, 1 + sum(maxChilds))
            return 1 + maxChilds[0]

        dfs(0)
        return ans