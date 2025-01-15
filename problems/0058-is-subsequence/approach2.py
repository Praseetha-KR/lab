class Solution:
    # Divide and conquer
    def is_sub_sequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if s[0] == t[0]:
            return self.is_sub_sequence(s[1:], t[1:])
        return self.is_sub_sequence(s, t[1:])

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.is_sub_sequence(s, t)
