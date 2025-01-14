from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                return True
        return False
