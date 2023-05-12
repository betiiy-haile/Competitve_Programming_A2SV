class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:        
        adjList = defaultdict(list)
        for bus in range(len(routes)):
            for station in routes[bus]:
                adjList[station].append(bus)

        busTaken = set()
        visited = set()
        queue = deque([(source, 0)])
        visited.add(source)

        while queue:
            station, busNo = queue.popleft()

            if station == target:
                return busNo 

            for buses in adjList[station]: 
                if buses not in busTaken: 
                    for end in routes[buses]: 
                        if end not in visited: 
                            queue.append((end, busNo+1))
                            visited.add(end)

                    busTaken.add(buses) 
                    
        return -1