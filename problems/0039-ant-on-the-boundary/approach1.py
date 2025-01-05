from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        displacement, crossing_count = 0, 0
        for n in nums:
            displacement += n
            if displacement == 0:
                crossing_count += 1
        return crossing_count
