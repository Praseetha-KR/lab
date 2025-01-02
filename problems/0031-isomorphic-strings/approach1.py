class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len1, len2 = len(s), len(t)
        if len1 != len2:
            return False

        m1, m2 = {}, {}
        for i in range(len1):
            if m1.get(s[i]) is None:
                if m2.get(t[i]) is None:
                    m1[s[i]] = t[i]
                    m2[t[i]] = s[i]
                    continue
                return False
            if m1[s[i]] == t[i] and m2[t[i]] == s[i]:
                continue
            return False
        return True
