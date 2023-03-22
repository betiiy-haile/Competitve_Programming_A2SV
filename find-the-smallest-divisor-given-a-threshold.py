class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def divide(k):
            sum = 0
            for num in nums:
                sum += ceil(num/k)
            return sum
        
        left = 1
        right = max(nums)  
        while left <= right:
            mid = left + (right - left)//2
            if divide(mid) > threshold:
                left = mid + 1           
            else :
                right = mid - 1
        return left