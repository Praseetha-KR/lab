class Solution:
    # Bottom up approach
    # Time complexity: O(N)
    # Space complexity: O(1)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        curr = 0
        prev1 = 1
        prev2 = 0
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr
