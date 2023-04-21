class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        arr = []
        for num in C.keys():
            arr.append([C[num] , num])

        arr = self.quickSort(arr)
        i = len(arr) - k
        ans = []

        while i < len(arr):
            ans.append(arr[i][1])
            i += 1

        return ans

    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for num in arr[1:]:
            if num[0] <= pivot[0]:
                left.append(num)
            else:
                right.append(num)
        
        return self.quickSort(left) + [pivot] + self.quickSort(right)