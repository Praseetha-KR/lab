class Solution:
    # Time complexity : O(log3(n)) (3 is the base)
    # Space complexity : O(1)
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
