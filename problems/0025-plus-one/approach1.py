from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end = digits[-1]
        prefix = digits[:-1]
        if end != 9:
            return prefix + [end + 1]

        res = []
        decimal = int("".join(map(str, digits))) + 1
        while decimal:
            res.append(decimal % 10)
            decimal //= 10
        return res[::-1]
