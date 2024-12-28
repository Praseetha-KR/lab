class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Bit by bit computation without zero-padding
        carry = 0
        res = ""

        al = list(a)
        bl = list(b)

        while al or bl or carry:
            if al:
                carry += int(al.pop())
            if bl:
                carry += int(bl.pop())

            res += str(carry % 2)
            carry //= 2

        return res[::-1]
