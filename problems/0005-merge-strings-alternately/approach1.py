class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Single pointer, append remaining

        res = []
        i = 0
        l1 = len(word1)
        l2 = len(word2)
        while i < l1 and i < l2:
            res += word1[i] + word2[i]
            i += 1

        if i < l1:
            res += word1[i:]
        else:
            res += word2[i:]
        return "".join(res)
