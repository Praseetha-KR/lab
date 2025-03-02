class Solution:
    # Greedy Way (Hash Set)
    # Time complexity: O(n)
    # Space complexity: O(1)

    def longestPalindrome(self, s: str) -> int:
        unmatched = set()
        res = 0
        for c in s:
            if c in unmatched:
                unmatched.remove(c)
                res += 2
            else:
                unmatched.add(c)
        if unmatched:
            res += 1
        return res
