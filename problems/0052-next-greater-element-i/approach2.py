from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i, n1 in enumerate(nums1):
            found = False
            for n2 in nums2:
                if n1 == n2:
                    found = True
                if found and n2 > n1:
                    res[i] = n2
                    break
        return res
