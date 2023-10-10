class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        distance = [[False] * numCourses for _ in range(numCourses)]
        
        for u, v in prerequisites:
            distance[u][v] = True
            
        for i in range(numCourses):
            distance[i][i] = 0
            
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if not distance[i][j]:
                        distance[i][j] = distance[i][k] and distance[k][j]
                        
                        
        ans = []
        for u, v in queries:
            ans.append(distance[u][v])
            
        return ans