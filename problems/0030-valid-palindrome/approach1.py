class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"

        s_processed = ""
        for c in s.lower():
            if c in chars:
                s_processed += c

        mid = len(s_processed) // 2
        for i in range(mid):
            if s_processed[i] != s_processed[-1 * (i + 1)]:
                return False
        return True