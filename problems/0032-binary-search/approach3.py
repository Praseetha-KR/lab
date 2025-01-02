from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find Lower bound
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if l < len(nums) and nums[l] == target:
            return l

        return -1
