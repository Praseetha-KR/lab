from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last_missing_number = 0
        missing_counter = 0
        n = 1
        arr_idx = 0
        while missing_counter < k:
            if arr_idx < len(arr) and arr[arr_idx] == n:
                arr_idx += 1
            else:
                last_missing_number = n
                missing_counter += 1
            n += 1
        return last_missing_number
