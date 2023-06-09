class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda i : (i[0], -i[1]))

        ans = len(intervals)
        longest = 0
        for start, end in intervals:
            if end <= longest:
                ans -= 1
            else:
                longest = end
        
        return ans