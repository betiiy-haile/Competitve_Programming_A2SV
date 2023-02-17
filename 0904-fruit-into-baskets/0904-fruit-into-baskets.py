class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first = -1
        second = -1
        secondCount = 0
        currMax = 0
        Max = 0
        
        for fruit in fruits:
            if fruit == first or fruit == second:
                currMax += 1
            else:
                currMax = secondCount + 1
        
            if fruit == second:
                secondCount += 1
            else:
                secondCount = 1
                
            if(fruit != second):
                first = second
                second = fruit
                
            Max = max(Max,currMax)
        return Max
            

        