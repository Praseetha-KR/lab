from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        i = 0
        for n in nums_sorted:
            if n != i:
                return i
            i += 1
        return i
