
class Solution:
    # Math: using Golden ratio approximation
    # Fn = φⁿ / √5
    # Ref: https://en.wikipedia.org/wiki/Fibonacci_sequence#Computation_by_rounding

    # Time complexity: O(logN)
    # Space complexity: O(1)
    def fib(self, n: int) -> int:
        phi = (1 + 5 ** 0.5) / 2
        return round(phi ** n / 5 ** 0.5)
