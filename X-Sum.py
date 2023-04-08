from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    maxsum = 0
    
    Sum = defaultdict(int)
    diff = defaultdict(int)

    for i in range(n):
        for j in range(m):
            Sum[i+j] += matrix[i][j]
            diff[i-j] += matrix[i][j]
    for i in range(n):
        for j in range(m):
            total = Sum[i+j] + diff[i-j]
            maxsum = max(maxsum, total - matrix[i][j])
    
    print(maxsum)
    