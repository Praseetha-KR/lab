from typing import List


class Solution:
    def binary_search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                l += 1
            else:
                r -= 1
        return -1

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            target = 2 * arr[i]
            target_index = self.binary_search(arr, target)
            if target_index >= 0 and target_index != i:
                return True
        return False
