class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        m = len(flights)

        for From, To,Prices in flights:
            graph[From].append((To, Prices))

        @cache
        def dp(target, stops):
            if target == dst: 
                return 0 
            if stops  == 0: 
                return float('inf') 
            ans = float('inf') 

            for neigh, weight in graph[target]: 
                ans = min(ans, weight + dp(neigh, stops -1))
            return ans 

        ans = dp(src, k + 1)
        return ans if ans != float("inf") else -1