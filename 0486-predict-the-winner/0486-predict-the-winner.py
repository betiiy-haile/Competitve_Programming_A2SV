class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums:
            return None
        def largeScore(small, large):
            if small > large:
                return 0
            
            
            return max(
                nums[small] - largeScore(small+1, large),
                nums[large] - largeScore(small, large-1)
            )
            
        return largeScore(0, len(nums)-1) >= 0