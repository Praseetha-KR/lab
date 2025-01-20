from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Brute Force
        # Time complexity: O(N)
        # Space complexity: O(1)
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k
