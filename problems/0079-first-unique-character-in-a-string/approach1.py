class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_map = {}
        for c in s:
            if c in unique_map:
                unique_map[c] = False
            else:
                unique_map[c] = True
        for i in range(len(s)):
            if unique_map[s[i]] is True:
                return i
        return -1
