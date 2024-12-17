class Solution:
    # reverse full number & compare

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_reverse = 0
        y = x
        while y > 0:
            l = y % 10
            x_reverse = x_reverse * 10 + l
            y = y // 10

        return x_reverse == x
