class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        target = "123450"
        start = "".join(str(num) for row in board for num in row)
        visited = set()

        directions = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]


        def swap(string, i, j):
            lst = list(string)
            lst[i], lst[j] = lst[j], lst[i]
            return "".join(lst)
        
        queue = deque()
        queue.append(start)
        visited.add(start)
        res = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == target:
                    return res
                
                zero = cur.index('0')
                for dir in directions[zero]:
                    next = swap(cur, zero, dir)
                    if next in visited:
                        continue
                    visited.add(next)
                    queue.append(next)
            res += 1
        
        return -1