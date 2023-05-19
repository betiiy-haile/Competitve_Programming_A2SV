num = input()
ans = input()
 
arr = []
for i in num:
    arr.append(i)
 
arr.sort()
for i in range(1, len(arr)):
    if arr[0] == '0' and arr[i] != '0':
        arr[0], arr[i] = arr[i], arr[0]
        break
 
if ans == ''.join(arr):
    print("OK") 
else:
    print("WRONG_ANSWER")