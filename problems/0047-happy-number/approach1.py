class Solution:
    def digit_square_sum(self, n: int):
        res = []
        while n > 0:
            res = [(n % 10) ** 2] + res
            n //= 10
        return sum(res)

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.digit_square_sum(n)
        return n == 1
