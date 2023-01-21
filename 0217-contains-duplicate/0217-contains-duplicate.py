class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        count = Counter(nums)
        for v,c in count.items():
            if c >= 2:
                return True
                break;
                
        return False 
        