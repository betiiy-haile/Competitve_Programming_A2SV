class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negativeCount = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negativeCount += 1
            nums[i] = abs(nums[i])

        d = defaultdict(int)
        for i in range(len(nums)):
            index = 0 
            while nums[i]:
                if nums[i] & 1 == 1:
                    d[index] += 1
                index += 1
                nums[i] >>= 1
        ans = 0
        for i,v in d.items():
            if v % 3 != 0:
                ans += 1 << i

        if negativeCount % 3 == 0:
            return ans
        return -ans