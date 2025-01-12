class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        i = 0
        j = 0
        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
                j += 1
            elif ransomNote[i] > magazine[j]:
                j += 1
            else:
                return False
        if i == len(ransomNote):
            return True
        return False
