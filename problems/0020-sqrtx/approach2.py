class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        l = 0
        r = x
        while l <= r:
            pivot = l + (r - l) // 2
            square = pivot * pivot
            if square <= x < (pivot + 1) * (pivot + 1):
                return pivot
            elif x < square:
                r = pivot - 1
                continue
            l = pivot + 1
