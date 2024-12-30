from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        curr_inc_subarr_len = 1
        prev_inc_subarr_len = 0

        max_adj_inc_subarr_size = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr_inc_subarr_len += 1
            else:
                prev_inc_subarr_len = curr_inc_subarr_len
                curr_inc_subarr_len = 1

            max_adj_inc_subarr_size = max(
                max_adj_inc_subarr_size,
                curr_inc_subarr_len // 2,
                min(prev_inc_subarr_len, curr_inc_subarr_len),
            )
        return max_adj_inc_subarr_size >= k
