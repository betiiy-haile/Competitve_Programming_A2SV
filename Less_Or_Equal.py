n , k = map(int, input().split())
nums = list(map(int , input().split()))

nums.sort()


if n == k:
    print(nums[-1])
elif k == 0:
    if nums[0] > 1:
        print(1)
    else:
        print(-1)
elif nums[k] != nums[k-1]:
    print(nums[k-1])
elif nums[k] == nums[k-1]:
    print(-1)