class Solution:
    # reverse half number & compare

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):  # non-zero last digit palindrome case
            return False

        x_reverse = 0
        while x > x_reverse:
            x_reverse = x_reverse * 10 + x % 10
            x //= 10

        return x == x_reverse or x == x_reverse // 10 # remove middle single digit
