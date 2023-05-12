class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        level = 0
        visited = set()

        while queue:
            for i in range(len(queue)):
                position, speed = queue.popleft()
                if position == target:
                    return level
                if (position + speed, speed * 2) not in visited:
                    queue.append((position + speed, speed * 2))
                    visited.add((position + speed, speed * 2))
                if speed > 0:
                    if (position, -1) not in visited:
                        queue.append((position, -1))
                        visited.add((position, -1))
                else:
                    if (position, 1) not in visited:
                        queue.append((position, 1))
                        visited.add((position, 1))

            level += 1