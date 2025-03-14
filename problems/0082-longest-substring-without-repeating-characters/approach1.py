class Solution:
    # Time limit exceeded!
    # Time complexity : O(n^3)
    # Space complexity : O(min(n,m)) where n: size of the string, m: size of the charset

    def is_all_unique_chars(self, s: str) -> bool:
        seen = set()
        for c in s:
            if c in seen:
                return False
            seen.add(c)
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        maxlen = 0
        for i in range(l):
            for j in range(i, l):
                if self.is_all_unique_chars(s[i: j + 1]):
                    maxlen = max(maxlen, j + 1 - i)
        return maxlen
