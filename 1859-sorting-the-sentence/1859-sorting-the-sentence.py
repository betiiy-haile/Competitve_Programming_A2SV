class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        result = ""

        for i in range(len(arr)):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j][-1] < arr[minIndex][-1]:
                    minIndex = j  
            if i != minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
            result += arr[i][:-1] + " "
        return result[:-1]


