class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        right = 0
        
        while right < len(numbers):
            if target - numbers[right] in d:
                break                
            d[numbers[right]] = right
            right += 1        
        left = d[target - numbers[right]] 
        
        return [left+1, right+1]