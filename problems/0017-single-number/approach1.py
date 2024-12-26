from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if m.get(n) is not None:
                del m[n]
                continue
            m[n] = True
        return list(m.keys())[0]
