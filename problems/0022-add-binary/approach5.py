class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Decimal conversion, compute sum, convert back to binary
        decimal_sum = int(a, 2) + int(b, 2)
        return f"{(decimal_sum):b}"
