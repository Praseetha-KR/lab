from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_magazine = Counter(magazine)
        for c in ransomNote:
            if c not in counter_magazine:
                return False
            if counter_magazine[c] <= 0:
                return False
            counter_magazine[c] -= 1
        return True
