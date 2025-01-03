from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        m = {a: i for i, a in enumerate(sorted(set(arr)))}
        return [m[a] + 1 for a in arr]
