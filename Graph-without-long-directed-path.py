from collections import defaultdict
 
n, m = map(int, input().split())
adjList = defaultdict(list)
edges = []
 
for _ in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])
    adjList[u].append(v)
    adjList[v].append(u)
 
colors = [-1] * n
 
def dfs(node, color):
    colors[node -1 ] = color
    stack = [node]
    while stack:
        curr = stack.pop()
 
        for child in adjList[curr]:
            if colors[child - 1] == -1:
 
                if colors[curr - 1] == colors[child - 1]:
                    return False
                                
                if colors[curr - 1] == 0: 
                    colors[child -1] = 1
                    stack.append(child)
                else:
                    colors[child - 1] = 0
                    stack.append(child)
            else:
                if colors[curr - 1] == colors[child - 1]:
                    return False
 
 
    return True
 
if not dfs(1, 1):
    print("NO")
    exit()
ans = []
for u, v in edges:
    ans.append(str(colors[u-1]))
 
print("YES")
print(''.join(ans))