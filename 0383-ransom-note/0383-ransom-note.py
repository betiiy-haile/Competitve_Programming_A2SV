class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        for ch in ransomNoteCount:
            if ch not in magazineCount or ransomNoteCount[ch] > magazineCount[ch]:
                return False
            
        return True
        
        