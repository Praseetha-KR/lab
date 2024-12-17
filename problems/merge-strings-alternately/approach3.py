class Solution:
    # for loop with maxlen
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l1 = len(word1)
        l2 = len(word2)
        maxlen = max(l1, l2)
        for i in range(maxlen):
            if i < l1:
                res += word1[i]
            if i < l2:
                res += word2[i]
        return "".join(res)
