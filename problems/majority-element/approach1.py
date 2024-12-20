from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        max_count = 0
        max_n = None
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] > max_count:
                max_count = counter[n]
                max_n = n
        return max_n
