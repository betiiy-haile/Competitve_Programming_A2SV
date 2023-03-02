class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = rightMax
            if temp > rightMax:
                rightMax = temp
        return arr
        