n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

edges = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            edges += 1

print(edges // 2)