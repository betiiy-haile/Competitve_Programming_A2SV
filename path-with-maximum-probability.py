class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        visited = set()
        graph = defaultdict(list)
        distances = [0] * n
        
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append(( v , prob))
            graph[v].append(( u , prob))
        
        heap = [(-1 , start)]
        while heap:
            prob , node = heappop(heap)
            prob = -prob

            if node in visited:
                continue
            visited.add(node)
            
            for Next, val in graph[node]:
                newProb = prob * val
                if newProb > distances[Next]:
                    distances[Next] = newProb
                    heappush(heap , (-newProb , Next))
        
        return distances[end]