class Solution:
    # Top down approach using memoization
    # Time complexity: O(N)
    # Space complexity: O(N)

    cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[-1]
