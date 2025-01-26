import bisect
from typing import List


class KthLargest:
    # Time Complexity: O(N^2+N⋅M)
    # Space Complexity: O(M+N)
    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.sorted_nums, val)
        return self.sorted_nums[-1 * self.k]
