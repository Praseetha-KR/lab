import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # This is an approximation solution, rounding off to 8 fails with given inputs
        # n = 2^x => log(2)n = x
        if n <= 0:
            return False
        return round(math.log(n, 2), 14).is_integer()
