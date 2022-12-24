class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1]=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                intervals[i]=[]

        ans = []        
        for i in intervals:
                if i!=[]:
                    ans.append(i)
        return ans