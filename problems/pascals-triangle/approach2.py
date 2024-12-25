from typing import List


class Solution:
    def pascal_triangle(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        if n == 1:
            return [[1]]

        prev_rows = self.pascal_triangle(n - 1)
        current_row = [
            1,
            *[prev_rows[-1][c - 1] + prev_rows[-1][c] for c in range(1, n - 1)],
            1,
        ]
        prev_rows.append(current_row)
        return prev_rows

    def generate(self, numRows: int) -> List[List[int]]:
        return self.pascal_triangle(numRows)
