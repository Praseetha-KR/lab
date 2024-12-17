class Solution:
    # Single pointer
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
        l = len(s)
        if l == 1:
            return self.SYMBOL_VALUE_MAP[s]
        
        i = 0
        while i < l:
            ds = self.DOUBLE_SYMBOL_VALUE_MAP.get(s[i:i + 2], None)
            if ds:
                res += ds
                i += 2
                continue
            res += self.SYMBOL_VALUE_MAP[s[i:i + 1]]
            i += 1
        return res