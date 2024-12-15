class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # backward filling
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
                continue
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
                continue
            # both equal
            nums1[k] = nums1[i]
            nums1[k - 1] = nums2[j]
            i -= 1
            j -= 1
            k -= 2
        
        # remaining
        if j >= 0:
            for r in range(j + 1):
                nums1[r] = nums2[r]
        return nums1
