class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        for c in t:
            m[c] = m.get(c, 0) - 1
        for count in m.values():
            if count != 0:
                return False
        return True
