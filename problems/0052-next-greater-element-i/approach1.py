from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n1 in nums1:
            found = False
            next_greater = -1
            for n2 in nums2:
                if n1 == n2:
                    found = True
                if found and n2 > n1:
                    next_greater = n2
                    break
            res.append(next_greater)
        return res
