N, D = map(int, input().split())
powers = list(map(int, input().split()))
 
powers.sort()
left = 0
right = N - 1
count = 0
 
while left <= right:
    summ = powers[right]
 
    while summ <= D and left < right:
        summ += powers[right]
        left += 1
 
    if summ > D:
        count += 1
 
    right -= 1
 
print(count)