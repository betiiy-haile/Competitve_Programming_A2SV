t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    idx = 0
    maxVal = 0
    totalSum = 0
 
    while idx < n:
        maxVal = arr[idx]
 
        if arr[idx] > 0:
            while idx < n and arr[idx] > 0:
                if maxVal < arr[idx]:
                    maxVal = arr[idx]
                
                idx += 1
 
        else:
            while idx < n and arr[idx] < 0:
                if maxVal < arr[idx]:
                    maxVal = arr[idx]
                idx += 1
 
        totalSum += maxVal
 
    print(totalSum)