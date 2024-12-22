from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        compressed_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[compressed_index] = nums[i]
                compressed_index += 1
        return compressed_index
