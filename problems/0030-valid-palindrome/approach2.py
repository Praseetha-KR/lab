class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = ""
        for c in s:
            if c.isalnum():
                processed_s += c
        processed_s = processed_s.lower()
        return processed_s == processed_s[::-1]
