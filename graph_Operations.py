from collections import defaultdict
vertices = int(input())
n = int(input())

graph = defaultdict(list)
for i in range(n):
    arr = list(map(int, input().split())) 
    if arr[0] == 1:
        graph[arr[1]].append(arr[2])
        graph[arr[2]].append(arr[1])
    else:
        print(*graph[arr[1]])