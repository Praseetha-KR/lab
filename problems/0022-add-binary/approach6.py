class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Bit by bit computation without zero-padding and without + operator
        x = int(a, 2)
        y = int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
