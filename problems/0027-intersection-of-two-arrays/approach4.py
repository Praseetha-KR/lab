from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        for n in nums1:
            seen[n] = True

        res = set()
        for n in nums2:
            if seen.get(n, False) is True:
                res.add(n)
        return list(res)
