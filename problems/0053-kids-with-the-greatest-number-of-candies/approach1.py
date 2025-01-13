from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        max_candy = max(candies)
        for i, c in enumerate(candies):
            if c + extraCandies >= max_candy:
                res[i] = True
        return res
