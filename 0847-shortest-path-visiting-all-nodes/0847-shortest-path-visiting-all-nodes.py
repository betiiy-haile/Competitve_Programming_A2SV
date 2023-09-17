class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        V = len(graph)
        curr_level = deque([(u, 1 << u) for u in range(V)])  
        all_visited = (1 << V) - 1  
        
        visited = [[False for bit_mask in range(0, all_visited + 1)] for _ in range(V)]
        
        for u in range(V):
            visited[u][1 << u] = True
        path_length = 0
        while curr_level:
            n = len(curr_level)
            while n:
                
                u, bit_mask = curr_level.popleft()
                if bit_mask == all_visited:
                    return path_length 
                
                
                for v in graph[u]:
                    
                    next_bit_mask = bit_mask | (1 << v)  
                    if visited[v][next_bit_mask]:
                        continue 
                    if next_bit_mask == all_visited: 
                        return path_length + 1
                    curr_level.append((v, next_bit_mask))
                    visited[v][next_bit_mask] = True 
                
                n -= 1
            path_length += 1
        
        
        return -1

        