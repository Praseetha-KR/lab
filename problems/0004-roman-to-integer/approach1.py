class Solution:
    # Double pointer
    SYMBOL_VALUE_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    DOUBLE_SYMBOL_VALUE_MAP = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    def romanToInt(self, s: str) -> int:
        res = 0
        s_len = len(s)
        if s_len == 1:
            return self.SYMBOL_VALUE_MAP[s]

        c = 0
        n = 1
        while n <= s_len:
            ds = self.DOUBLE_SYMBOL_VALUE_MAP.get(s[c:n + 1], None)
            if ds:
                res += ds
                c += 2
                n += 2
                continue
            res += self.SYMBOL_VALUE_MAP[s[c:n]]
            c += 1
            n += 1
        return res
