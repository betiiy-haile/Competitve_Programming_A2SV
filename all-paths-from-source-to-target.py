class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def dfs(path, next):            
            if next == len(graph) - 1:
                paths.append(path[:])

            for neighbour in graph[next]:  
                path.append(neighbour)                  
                dfs(path, neighbour)
                path.pop()
                
        dfs([0], 0)
        return paths