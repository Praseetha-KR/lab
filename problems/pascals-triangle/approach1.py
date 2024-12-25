from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        rows = [[1]]
        for r in range(1, numRows):
            row = [
                1,
                *[(rows[r - 1][c - 1] + rows[r - 1][c]) for c in range(1, r)],
                1,
            ]
            rows.append(row)
        return rows
