from typing import List


class Solution:
    # Time complexity: O(M⋅N)
    # Space complexity: O(1)

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth_so_far = 0
        for account in accounts:
            max_wealth_so_far = max(sum(account), max_wealth_so_far)
        return max_wealth_so_far
