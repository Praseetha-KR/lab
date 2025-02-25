class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Two pointers

        res = []
        i = 0
        j = 0
        l1 = len(word1)
        l2 = len(word2)

        while i < l1 or j < l2:
            if i < l1:
                res += word1[i]
                i += 1
            if j < l2:
                res += word2[j]
                j += 1

        return "".join(res)
