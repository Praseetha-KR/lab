# The isBadVersion API is already defined.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid): # type: ignore  # noqa: F821
                r = mid
            else:
                l = mid + 1
        return l
