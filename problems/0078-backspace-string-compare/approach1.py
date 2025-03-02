class Solution:
    def rendered_string(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if s[i] == "#":
                res = res[:-1]
            else:
                res += s[i]
        return res

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.rendered_string(s) == self.rendered_string(t)
