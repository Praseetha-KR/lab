from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = {}
        m2 = {}
        for n in nums1:
            m1[n] = m1.get(n, 0) + 1
        for n in nums2:
            m2[n] = m2.get(n, 0) + 1

        intersection = []
        for k in m1:
            if m2.get(k, 0) > 0:
                intersection.append(k)
        return intersection
