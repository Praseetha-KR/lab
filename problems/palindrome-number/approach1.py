import math


class Solution:
    # str conversion, half front & rear comparison

    def isPalindrome(self, x: int) -> bool:
        xs = str(x)
        mid = math.floor(len(xs) / 2)

        for i in range(mid):
            if xs[i] != xs[-i - 1]:
                return False
        return True
