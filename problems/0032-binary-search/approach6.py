from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return binary_search(mid + 1, r)
            return binary_search(l, mid - 1)
        return binary_search(0, len(nums) - 1)
