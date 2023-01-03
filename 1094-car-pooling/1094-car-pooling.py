class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
             
        lengthOfTrip = [0]*1001 
        for trip, i, j in trips:
            lengthOfTrip[i] += trip 
            lengthOfTrip[j] -= trip 
            
        current = 0
        for i in range( len(lengthOfTrip) ):
            current += lengthOfTrip[i] 
            if current > capacity: 
                return False               
            
        return True 

                