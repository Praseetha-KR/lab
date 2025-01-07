from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l == r:
            if target > nums[l]:
                return l + 1
            return l

        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return self.binary_search(nums, target, l, mid)
        return self.binary_search(nums, target, mid + 1, r)

    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        return self.binary_search(nums, target, l, r)
