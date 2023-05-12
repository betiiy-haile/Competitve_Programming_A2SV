
t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    ans = 0
    mult = 1
 
    for i in range(32):
        if k & (1 << i):
            ans = (ans + mult) % ((10 ** 9) + 7)
        mult *= n
        mult %= ((10 ** 9) + 7)
 
    print(ans)