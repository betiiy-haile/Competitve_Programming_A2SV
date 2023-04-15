n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


left = 0
ans = [] 
for num in arr2:
    while left < n and arr1[left] < num:
        left += 1
    ans.append(left)
    
print(*ans)