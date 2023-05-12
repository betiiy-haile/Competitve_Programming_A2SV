t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    even = 1
    for j in range(n):
        while nums[j]%2 == 0:
            even *= 2
            nums[j] /= 2
    maxNum = max(nums)
    Total = sum(nums) + ((even-1) * maxNum)
    print(int(Total))