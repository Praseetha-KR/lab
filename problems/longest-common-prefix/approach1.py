from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = ""
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            curr = ""
            for s in strs:
                if curr == "":
                    curr = s[i]
                elif s[i] != curr:
                    return res
            res += curr
        return res
