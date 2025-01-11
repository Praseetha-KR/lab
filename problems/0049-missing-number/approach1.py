from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            m[n] = True
        for i in range(len(nums)):
            if m.get(i) is None:
                return i
        return i + 1
