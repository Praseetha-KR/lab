from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        for i in range(arr_len):
            for j in range(arr_len):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
