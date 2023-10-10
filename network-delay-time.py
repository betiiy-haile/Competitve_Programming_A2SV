class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(dict)

        for start, end, weight in times:
            graph[start][end] = weight

        distances = {i+1: float('inf') for i in range(n)}
        distances[k] = 0
        heap = [(0,k)]
        visited = set()

        while heap:
            distance,node  = heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            for neighbor,weight in graph[node].items():
                if distance + weight < distances[neighbor]:
                    distances[neighbor] = distance + weight
                    heappush(heap,(distance + weight,neighbor))

        result = max(distances.values())
        
        return result if result != float('inf') else -1