from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = consecutive = 0
        for n in nums:
            consecutive = consecutive * n + n
            max_count = max(max_count, consecutive)
        return max_count
