class Solution:
    # Recursion - DP

    def climb(self, n: int, m: dict):
        if n == 0 or n == 1:
            return 1
        if n not in m:
            m[n] = self.climb(n - 1, m) + self.climb(n - 2, m)
        return m[n]

    def climbStairs(self, n: int) -> int:
        m = {}
        return self.climb(n, m)
