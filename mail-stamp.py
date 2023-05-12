from collections import defaultdict, deque
n = int(input())
graph = defaultdict(list)
cities = set()
for _ in range(n):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
 
src = []
for x,y in graph.items():
    if len(y) == 1:
        src.append(x)
 
path = []
queue = deque([src[1]])
visited = set()
while queue:
    curr = queue.popleft()
    visited.add(curr)
    path.append(curr)
    for child in graph[curr]:
        if child not in visited:
            queue.append(child)
 
print(*path)