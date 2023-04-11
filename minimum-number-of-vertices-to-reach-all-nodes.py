class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        graph = defaultdict(list)
        for x,y in edges:
            graph[y].append(x)
        
        ans = []
        for i in range(n):
            if graph[i] == []:
                ans.append(i)
        
        return ans