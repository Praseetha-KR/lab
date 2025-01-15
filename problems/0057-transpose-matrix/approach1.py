from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = [[None] * rows for _ in range(cols)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                res[c][r] = val
        return res
