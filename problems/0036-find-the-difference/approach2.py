class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s, sorted_t = sorted(s), sorted(t)
        for i in range(len(t)):
            if len(s) - 1 < i or sorted_t[i] != sorted_s[i]:
                return sorted_t[i]
