from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        # Time limit exceeded
        res = []
        start = end = None
        i = 0
        n = lower
        while n <= upper and i < len(nums):
            if n == nums[i]:
                if start is not None:
                    res.append([start, end])
                    start = end  = None
                i += 1
            elif n < nums[i]:
                if start is None:
                    start = n
                end = n
            n += 1
        if n <= upper:
            res.append([n, upper])
        return res

