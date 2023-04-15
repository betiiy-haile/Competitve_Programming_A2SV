n = int(input())
arr = list(map(int, input().split()))

odd = False
even = False

for num in arr:
    if num % 2 == 0:
        even = True
    else:
        odd =  True

if even and odd:
    print(*(sorted(arr)))
else:
    print(*(arr))