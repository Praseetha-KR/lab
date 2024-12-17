class Solution:
    # Recursion - unoptimized - Fails with time limit exceeded

    def climb(self, n: int):
        if n == 0 or n == 1:
            return 1
        return self.climb(n - 1) + self.climb(n - 2)

    def climbStairs(self, n: int) -> int:
        return self.climb(n)
