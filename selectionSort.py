class Solution: 
    def select(self, arr, i):
        selectionSort(arr,len(arr))
         
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            minIndex = i
            for j in range(i+1,n):
                if(arr[j] < arr[minIndex]):
                    minIndex = j;
            if minIndex != i:
                arr[i], arr[minIndex]= arr[minIndex], arr[i]
        
