from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(0, len(nums) - k + 1):
            k_counter = sorted(
                Counter(nums[i:i + k]).most_common(),
                key=lambda x: (-x[1], -x[0])
            )[:x]
            k_sum = 0
            for key, val in k_counter:
                k_sum += key * val
            res.append(k_sum)
        return res
