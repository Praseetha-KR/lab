from typing import List


class Solution:
    def is_increasing(self, arr: List[int]) -> bool:
        return all([arr[i] < arr[i + 1] for i in range(len(arr) - 1)])

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        for i in range(n - 2 * k + 1):
            subarray1 = nums[i:i + k]
            subarray2 = nums[i + k:i + 2 * k]
            if self.is_increasing(subarray1) and self.is_increasing(subarray2):
                return True

        return False
