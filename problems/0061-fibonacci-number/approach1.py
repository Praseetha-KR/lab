class Solution:
    # Recursion
    # Time complexity: O(2^N)
    # Space complexity: O(N)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
