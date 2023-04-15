t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = True
    for i in range(1, n):
        if nums[i] - 1 > nums[i-1]:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")