class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        i = 0
        while i * i < x:
            i += 1

        if i * i == x:
            return i
        return i - 1
