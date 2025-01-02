from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_zero_pos], nums[i] = nums[i], nums[last_zero_pos]
                last_zero_pos += 1
