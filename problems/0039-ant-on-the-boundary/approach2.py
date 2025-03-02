from itertools import accumulate
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum(n == 0 for n in accumulate(nums))
