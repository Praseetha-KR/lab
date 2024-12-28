class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a_filled = a.zfill(maxlen)
        b_filled = b.zfill(maxlen)
        a_b_carry_to_sum_carry_map = {
            "000": (0, 0),
            "001": (1, 0),
            "010": (1, 0),
            "011": (0, 1),
            "100": (1, 0),
            "101": (0, 1),
            "110": (0, 1),
            "111": (1, 1),
        }
        carry = 0
        res = ""
        for i in range(maxlen -1, -1, -1):
            r, carry = a_b_carry_to_sum_carry_map[f"{a_filled[i]}{b_filled[i]}{carry}"]
            res = f"{r}{res}"
        if carry == 1:
            res = f"{carry}{res}"
        return res
