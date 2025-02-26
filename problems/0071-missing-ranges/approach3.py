from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        # Time complexity: O(n)
        # Space complexity: O(1)

        missing_ranges = []
        for n in nums + [upper + 1]:
            if n > lower:
                missing_ranges.append([lower, n - 1])
            lower = n + 1
        return missing_ranges
