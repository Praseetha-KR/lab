class Solution:
    # Bottom up approach space optimized
    # Time complexity: O(N)
    # Space complexity: O(1)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        memo = [0, 1]
        for _ in range(2, n + 1):
            memo = [memo[-1], memo[-1] + memo[-2]]
        return memo[-1]
