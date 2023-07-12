class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if edges == []:
            return [0] 

        adjList = defaultdict(list)
        indegree = [0] * n

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        queue = deque()
        visited = set()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                visited.add(i)

        ans = []
        while queue:
            ans = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                ans.append(curr)
                for neighbour in adjList[curr]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 1 and neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)

        return ans