class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def get_pattern(s: str):
            return tuple(s.index(c) for c in s)
        return get_pattern(s) == get_pattern(t)
