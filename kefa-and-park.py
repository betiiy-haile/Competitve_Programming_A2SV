n, m = map(int, input().split())
count = list(map(int, input().split()))

adjList = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    adjList[a - 1].append(b - 1)
    adjList[b - 1].append(a - 1)


def dfs(start, parent, cats):
    stack = [(start, parent, cats)]
    leafCount = 0
    while stack:
        current, parent, currentCats = stack.pop()
        if currentCats > m:
            continue
        is_leaf = True
        for neighbor in adjList[current]:
            if neighbor != parent:
                is_leaf = False
                stack.append((neighbor, current, currentCats * count[neighbor] + count[neighbor]))
        leafCount += is_leaf
    return leafCount


ans = dfs(0, -1, count[0])
print(ans)