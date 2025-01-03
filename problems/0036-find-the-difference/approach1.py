class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        for c in t:
            count = m.get(c, None)
            if count is None:
                return c
            m[c] = count - 1
        for k, v in m.items():
            if v != 0:
                return k
        return ""
