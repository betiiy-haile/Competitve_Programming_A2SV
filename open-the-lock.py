class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        start = "0000"
        queue = deque([(start)])

        if start in visited:
            return -1

        def getNextMove(curr):
            neighbours = []
            for i in range(4):
                val = str((int(curr[i]) + 1) % 10)
                neighbours.append(curr[:i] + val + curr[i+1:])
                val = str((int(curr[i]) - 1) % 10)
                neighbours.append(curr[:i] + val + curr[i+1:])
            return neighbours

        level = 0
        while queue:
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if curr == target:
                    return level
                    
                neighbours =  getNextMove(curr)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
            level += 1

        return -1