from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.sorted_nums = sorted(self.sorted_nums + [val])
        return self.sorted_nums[-1 * self.k]
