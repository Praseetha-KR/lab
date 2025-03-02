class Solution:
    # Using digital root property: https://en.wikipedia.org/wiki/Digital_root
    # Time complexity: O(1)
    # Space complexity: O(1)
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
