from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Cumulative sum
        l = len(nums)
        csum = [0] * l
        csum[0] = nums[0]
        for i in range(1, l):
            csum[i] = csum[i - 1] + nums[i]

        max_sum = csum[k - 1]
        for i in range(k, l):
            max_sum = max(max_sum, csum[i] - csum[i - k])
        return max_sum / k
