class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = []
        self.leftSum = 0
        for i in range(len(nums)):
            self.leftSum +=nums[i]
            self.preSum.append(self.leftSum) 


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.preSum[right]
        else:
            return self.preSum[right] - self.preSum[left-1]
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)