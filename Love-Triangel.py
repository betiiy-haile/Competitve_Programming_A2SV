n = int(input())
nums = list(map(int, input().split()))
for i in range(1, n):
    if nums[nums[nums[i-1]-1]-1] == i:
        print('YES')
        exit()
print('NO')