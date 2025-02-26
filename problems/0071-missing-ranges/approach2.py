from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        # Time complexity: O(n)
        # Space complexity: O(1)

        l = len(nums)
        if l == 0:
            return [[lower, upper]]

        missing_ranges = []
        if nums[0] > lower:
            missing_ranges.append([lower, nums[0] - 1])
        for i in range(1, l):
            if nums[i] != nums[i - 1] + 1:
                missing_ranges.append([nums[i - 1] + 1, nums[i] - 1])
        if nums[-1] < upper:
            missing_ranges.append([nums[-1] + 1, upper])
        return missing_ranges
