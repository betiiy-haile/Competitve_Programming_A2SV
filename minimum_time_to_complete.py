from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        adjList = defaultdict(list)
        indegree = [0] * n
        
        for a, b in edges:
            adjList[a -1].append(b-1)
            indegree[b-1] += 1
            
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        ans = [0] * n
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                ans[curr] = level
                for neighbour in adjList[curr]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
                
        return ans