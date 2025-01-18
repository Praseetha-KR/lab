import math


class Solution:
    # Math: using Golden ratio
    # φ (phi) = (1 + √5) / 2 ≈ 1.618033989 (the golden ratio)
    # ψ (psi) = (1 - √5) / 2 ≈ -0.618033989 = -1/φ = -φ⁻¹
    # Fn = (φⁿ - ψⁿ) / √5 = (φⁿ - -φ⁻ⁿ) / √5
    # Ref: https://en.wikipedia.org/wiki/Fibonacci_sequence#Closed-form_expression

    # Time complexity: O(logN)
    # Space complexity: O(1)
    def fib(self, n: int) -> int:
        phi = (1 + math.sqrt(5)) / 2
        return round((phi ** n - (-phi ** -n)) / math.sqrt(5))
