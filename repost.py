from collections import defaultdict, deque
n = int(input())
reposts = []
for _ in range(n):
    repost = list(map(str, input().split()))
    reposts.append(repost) 
 
graph = defaultdict(list)
for x,y,z in reposts:
    graph[z.lower()].append(x.lower()) 
 
visited = set()
queue = deque(["polycarp"])
level = 0
while queue:
    for i in range(len(queue)):
        curr = queue.popleft()
        visited.add(curr)
        for next in graph[curr]:
            if next not in visited:
                queue.append(next)  
    level += 1
print(level)