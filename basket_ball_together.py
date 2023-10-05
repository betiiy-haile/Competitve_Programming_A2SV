import math
 
N, D = map(int, input().split(" "))
players = list(map(int, input().split(" ")))
players.sort(reverse=True)
count = 0
left = 0
right = len(players)-1
while left <= right:
    x = math.floor((D / players[left]) + 1)
    if x <= right-left+1:
        count += 1
        left += 1
        right -= x-1
    else:
        break
 
print(count)