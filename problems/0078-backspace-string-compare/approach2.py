class Solution:
    # Time Complexity: O(M+N)
    # Space Complexity: O(M+N)

    def rendered_string(self, s: str) -> str:
        res = []
        for c in s:
            if c != "#":
                res.append(c)
            elif res:
                res.pop()
        return "".join(res)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.rendered_string(s) == self.rendered_string(t)
