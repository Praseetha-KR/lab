class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c not in bracket_pairs:
                stack.append(c)
                continue

            if not stack:
                return False

            pair = bracket_pairs[c]
            top = stack.pop()
            if pair != top:
                return False
        return not stack
