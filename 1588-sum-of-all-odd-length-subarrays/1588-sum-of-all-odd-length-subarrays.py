class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0;
        freq = 0;
        n = len(arr)
        for i in range(n):
            freq = freq-(i+1)//2+(n-i+1)//2
            ans += freq*arr[i]
        return ans

