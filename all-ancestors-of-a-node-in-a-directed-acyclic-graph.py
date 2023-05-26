class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        inDegree = [0] * n

        for x, y in edges:
           adjList[x].append(y)
           inDegree[y] += 1

        queue = deque()
        for i in range(n):
            if inDegree[i] == 0:
                queue.append(i)

        ancestors = defaultdict(set)
        while queue:
            curr = queue.popleft()
            for child in adjList[curr]:
                ancestors[child].add(curr)

                for ancestor in ancestors[curr]:
                    ancestors[child].add(ancestor)

                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child) 

        ans = [[] for _ in range(n)]
        for i in range(n):
            ans[i] = list(sorted(ancestors[i]))
        
        return ans