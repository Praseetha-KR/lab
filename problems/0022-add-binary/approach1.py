class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a_filled = a.zfill(maxlen)
        b_filled = b.zfill(maxlen)
        carry = 0
        res = ""
        for i in range(maxlen -1, -1, -1):
            r = 0
            if a_filled[i] == "0" and b_filled[i] == "0":
                if carry == 1:
                    r = 1
                else:
                    r = 0
                carry = 0
            elif a_filled[i] == "0" and b_filled[i] == "1":
                if carry == 1:
                    r = 0
                    carry = 1
                else:
                    r = 1
                    carry = 0
            elif a_filled[i] == "1" and b_filled[i] == "0":
                if carry == 1:
                    r = 0
                    carry = 1
                else:
                    r = 1
                    carry = 0
            elif a_filled[i] == "1" and b_filled[i] == "1":
                if carry == 1:
                    r = 1
                else:
                    r = 0
                carry = 1
            res = f"{r}{res}"

        if carry == 1:
            res = f"{carry}{res}"
        return res
