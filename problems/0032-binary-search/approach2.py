from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find Upper bound
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        if l > 0 and nums[l - 1] == target:
            return l - 1

        return -1
