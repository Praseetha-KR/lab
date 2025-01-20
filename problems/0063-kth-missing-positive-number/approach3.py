from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Binary Search
        # Time complexity: O(logN)
        # Space complexity: O(1)
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k
