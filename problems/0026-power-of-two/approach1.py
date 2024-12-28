class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = {}
        for i in range(32):
            power = 2**i
            m[power] = i
            if power > n:
                break
        return n in m
