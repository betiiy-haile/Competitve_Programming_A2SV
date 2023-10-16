class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)    
            graph[v].append(u)    
        
        count = 0
        def dfs(node, parent):

            nonlocal count
            total = values[node]

            for neigh in graph[node]:
                if neigh != parent:
                    total += dfs(neigh, node)
                print(total)
            if total % k == 0:
                count += 1
                return 0
            
            return total

        val = dfs(0, -1)
        return count