from typing import List


class Solution:
    # Naive Linear Search
    # Time complexity : O(nmin(k,n))
    # Space complexity : O(1)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(max(i - k, 0), i):
                if (nums[i] == nums[j]):
                    return True
        return False
