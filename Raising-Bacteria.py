n = int(input())
count = 0
while n != 0:
    while n % 2 == 0:
        n //= 2
    else:
        n -= 1
    count += 1
 
print(count)