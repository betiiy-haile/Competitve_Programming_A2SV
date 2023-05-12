class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjlist = defaultdict(list)
        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        ans = [0] * n

        def dfs(node,parent):
            count = Counter()
            for child in adjlist[node]:
                if child != parent:
                    count += dfs(child,node)
            count[labels[node]] += 1
            ans[node] = count[labels[node]]
            return count
            
        dfs(0,-1)
        return ans