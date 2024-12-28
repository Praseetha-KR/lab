class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Bit by bit computation - single carry
        maxlen = max(len(a), len(b))
        a_filled = a.zfill(maxlen)
        b_filled = b.zfill(maxlen)

        carry = 0
        res = []

        for i in range(maxlen - 1, -1, -1):
            if a_filled[i] == "1":
                carry += 1
            if b_filled[i] == "1":
                carry += 1
            if carry % 2 == 1:
                res.append("1")
            else:
                res.append("0")
            carry = carry // 2

        if carry == 1:
            res.append("1")

        res.reverse()
        return "".join(res)
