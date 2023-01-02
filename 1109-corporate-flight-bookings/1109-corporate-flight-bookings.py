class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*n
        
        for start,end,value in bookings:
            ans[start-1] += value
            if end < n:
                ans[end] -= value
        
        for i in range(1,len(ans)):
            ans[i] += ans[i -1]
        
        return ans