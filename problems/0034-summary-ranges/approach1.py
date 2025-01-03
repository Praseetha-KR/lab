from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l = len(nums)
        if l == 0:
            return []

        def display_range(start_idx: int, end_idx: int) -> None:
            if start_idx >= end_idx:
                res.append(f"{nums[start_idx]}")
                return
            res.append(f"{nums[start_idx]}->{nums[end_idx]}")

        start_idx = 0
        end_idx = l - 1
        for i in range(l - 1):
            if nums[i] + 1 != nums[i + 1]:
                end_idx = i
                display_range(start_idx, end_idx)
                start_idx = i + 1

        end_idx = l - 1
        display_range(start_idx, end_idx)
        return res
