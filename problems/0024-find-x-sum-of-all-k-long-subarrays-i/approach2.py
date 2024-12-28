import heapq
from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(0, len(nums) - k + 1):
            k_counter = [(count, key) for key, count in Counter(nums[i:i + k]).items()]
            x_largest = heapq.nlargest(x, k_counter)
            res.append(sum(key * count for count, key in x_largest))
        return res
