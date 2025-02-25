class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1):
            if haystack[i] == needle[0]:
                if i + l2 <= l1 and haystack[i:i + l2] == needle:
                    return i
        return -1
