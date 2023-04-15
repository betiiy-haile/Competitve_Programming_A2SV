n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

first = 0
second = 0
ans = []
while first < n and second < m:
    if arr1[first] < arr2[second]:
        ans.append(arr1[first])
        first += 1
    else:
        ans.append(arr2[second])
        second += 1

ans.extend(arr1[first:])
ans.extend(arr2[second:])
print(*ans)