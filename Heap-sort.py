class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        
        largest = i  
        left = 2 * i + 1     
        right = 2 * i + 2     
        if left < n and arr[largest] < arr[left]:
            largest = left
     
        if right < n and arr[largest] < arr[right]:
            largest = right
     
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
     
            self.heapify(arr, n, largest)
            
    def head_up(self, heap, current):
        parent = (current - 1) //  2 
        if current > 0 and heap[current] < heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
            self.heap_up(heap, parent)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        heap = []
        
        for num in arr:
            heap.append(num)
            current = len(heap) - 1
            self.heap_up(heap, current)
            
        return heap
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        N = len(arr)
 
        # Build a maxheap.
        for i in range(N//2 - 1, -1, -1):
            self.heapify(arr, N, i)
     
        # One by one extract elements
        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            self.heapify(arr, i, 0)
