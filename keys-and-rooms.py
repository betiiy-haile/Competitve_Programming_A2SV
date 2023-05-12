class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        visited = set()
        visited.add(0)

        while queue:
            curr = queue.popleft()
            visited.add(curr)

            for child in rooms[curr]:
                if child not in visited and child not in queue:
                    queue.append(child)

        return True if len(visited) == len(rooms) else False