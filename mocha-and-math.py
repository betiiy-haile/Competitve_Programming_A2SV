t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split())) 
    ans = arr[0]
    for i in range(n):
        ans &= arr[i]
    print(ans)