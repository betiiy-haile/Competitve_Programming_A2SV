class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            x = self.getRow(rowIndex-1)
            new = [1]
            for i in range(len(x)-1):
                new.append(x[i] + x[i+1])
            new.append(1)
            return new
        
        