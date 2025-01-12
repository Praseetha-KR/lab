from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransom = Counter(ransomNote)
        for c in magazine:
            if c in counter_ransom:
                counter_ransom[c] -= 1
        return all(counter_ransom[c] <= 0 for c in counter_ransom)
