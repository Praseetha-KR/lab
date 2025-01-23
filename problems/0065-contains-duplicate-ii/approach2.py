from typing import List


class Solution:
    # Hash Table
    # Time complexity : O(n)
    # Space complexity : O(min(n,k))
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i, n in enumerate(nums):
            if n in m and i - m[n] <= k:
                return True
        return False
