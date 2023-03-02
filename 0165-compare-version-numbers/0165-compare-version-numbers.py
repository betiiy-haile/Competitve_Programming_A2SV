class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))  
        version2 =list(map(int, version2.split('.')))  
        
        for x, y in zip_longest(version1, version2, fillvalue=0):
            if x == y:
                continue

            return -1 if x < y else 1 
        return 0