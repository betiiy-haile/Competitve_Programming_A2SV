class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adjList = defaultdict(list)
        tickets = sorted(tickets, reverse=True)
        
        for From, To in tickets:
            adjList[From].append(To)
            
        ans = []
        def dfs(src):
            while adjList[src]:
                Next = adjList[src].pop() 
                dfs(Next)
            ans.append(src)
        
        dfs("JFK")        
        return ans[::-1]
        