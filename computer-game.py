from collections import deque
t = int(input())
 
for _ in range(t):
    grid = [] 
    cols = int(input())
    for i in range(2):
        row = input()
        grid.append(row)
    directions = [(0,1), (0, -1), (1,0), (-1, 0), (-1,-1), (-1, 1),(1, -1), (1, 1)]
    visited = set()
    ans = 'NO'
    queue = deque()
    queue.append((0, 0))
    while queue:
        for i in range(len(queue)):
            row, col = queue.popleft()
            if row == 1 and col == cols-1:
                ans = "YES"
                break
            for x,y in directions:
                r = row + x
                c = col + y
                if 0 <= r < 2 and 0 <= c < cols and (r, c) not in visited and grid[r][c] != '1':
                    queue.append((r,c))
                    visited.add((r,c))
 
    print(ans)