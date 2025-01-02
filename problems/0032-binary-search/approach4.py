import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_right(nums, target)
        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        return -1
