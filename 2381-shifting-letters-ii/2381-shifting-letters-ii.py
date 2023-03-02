class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        
        for start, end, dxn in shifts:
            if dxn == 1:
                prefix[start] += 1
                prefix[end+1] -= 1
            else:
                prefix[start] -= 1
                prefix[end+1] += 1
                
        ans = []
        for i,c in enumerate(s):
            shift = prefix[i]
            ans.append(chr(((ord(c)-97+shift)%26)+97))
            prefix[i+1] += prefix[i]
            
        return ''.join(ans)