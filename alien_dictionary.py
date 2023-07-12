#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(N - 1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    adjList[word1[i]].append(word2[i])
                    indegree[word2[i]] += 1
                    break
                    
        queue = deque()
        for i in range(K):
            if indegree[chr(i + 97)] == 0:
                queue.append(chr(i + 97))
        
        order = []        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbour in adjList[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return "".join(order)
            
    
