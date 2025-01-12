from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        for n2 in nums2:
            while stack and n2 > stack[-1]:
                m[stack.pop()] = n2
            stack.append(n2)
        return [m.get(n1, -1) for n1 in nums1]
