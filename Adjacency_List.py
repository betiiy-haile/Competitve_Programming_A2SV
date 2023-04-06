from collections import defaultdict
n = int(input())
adjList = defaultdict(list)
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            adjList[i+1].append(j+1)

for k,v in adjList.items():
    print(len(v), *v)

