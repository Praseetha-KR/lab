from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows = len(accounts)
        cols = len(accounts[0]) if rows > 0 else 0
        wealth = [0] * rows
        for i in range(rows):
            for j in range(cols):
                wealth[i] += accounts[i][j]
        return max(wealth)
