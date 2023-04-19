count = 0 
def mergeSort(arr, low, high):

    if low == high:
        return [arr[low]]
    
    mid = low + (high - low)//2
    left = mergeSort(arr, low, mid)
    right = mergeSort(arr, mid+1, high)
    
    return merge(left, right)
 
def merge(left, right):
    global count
    Sorted = []
    if left[0] < right[0]:
        Sorted = left + right
    else:
        count += 1
        Sorted = right + left
 
    return Sorted
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = mergeSort(arr, 0, n-1)
    arr.sort()
    if answer == arr:
        print(count)
    else:
        print(-1)
    count = 0