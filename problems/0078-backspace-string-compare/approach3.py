import itertools


class Solution:
    # Time Complexity: O(M+N)
    # Space Complexity: O(1)

    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(s):
            skip = 0
            for c in reversed(s):
                if c == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c
        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))
