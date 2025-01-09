from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding window with Kadane's algorithm
        current_sum = best_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            best_sum = max(best_sum, current_sum)
        return best_sum / k
