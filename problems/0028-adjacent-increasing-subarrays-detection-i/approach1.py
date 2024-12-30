from typing import List


class Solution:
    def is_sorted(self, arr: List[int]) -> bool:
        prev = float('-inf')
        for n in arr:
            if prev >= n:
                return False
            prev = n
        return True

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - k):
            arr1 = nums[i:i + k]
            arr2 = nums[i + k:i + 2 * k]
            if len(arr2) < k:
                return False
            if self.is_sorted(arr1) and self.is_sorted(arr2):
                return True
        return False
