from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        l = sorted_nums[0]
        h = sorted_nums[-1]
        for i in range(len(nums)):
            shifted_nums = nums[i:] + nums[:i]
            if shifted_nums[0] == l and shifted_nums[-1] == h:
                return sorted_nums == shifted_nums
        return False
