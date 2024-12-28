from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for n in arr:
            m[n] = m.get(n, 0) + 1
        return len(m) == len(set(m.values()))
