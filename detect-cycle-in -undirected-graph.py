from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    visited = set()
	    def dfs(node, parent):
	        for child in adj[node]:
	            if child != parent:
    	            if child in visited:
    	                return True
                    else:
                        visited.add(child)
                        if dfs(child, node):
                            return True
            return False
        
        for i in range(V):
            if i not in visited:
                visited.add(i)
                if dfs(i, None):
                    return True
                    
        return False
            