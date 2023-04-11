class Solution(object):
    def maximalNetworkRank(self, n, roads):
        ans = 0
        adjList = defaultdict(list)
        for x,y in roads:
            adjList[x].append(y)
            adjList[y].append(x)

        for i in range(n):
            for j in range(i+1, n):
                curr = len(adjList[i]) + len(adjList[j]) 
                if i in adjList[j]:
                    curr -= 1
                ans = max(ans, curr)

        return ans