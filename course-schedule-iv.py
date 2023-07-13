class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adjList[a].append(b)
            indegree[b] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = defaultdict(set)                
        while queue:
            curr = queue.popleft()
            for neighbour in adjList[curr]:
                indegree[neighbour] -= 1
                res[neighbour].add(curr)
                res[neighbour].update(res[curr])
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        ans = []
        for x, y in queries:
            ans.append(x in res[y])
        
        return ans