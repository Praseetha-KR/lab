from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for n in nums:
            if n in m:
                return True
            m[n] = True
        return False
