class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # shift right leaving space for n elements
        for i in range(m + n - 1, n - 1, -1):
            nums1[i] = nums1[i - n]
            
        i = n
        j = 0
        k = 0
        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                k += 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
                k += 1
            else: # both equal
                nums1[k] = nums1[i]
                i += 1
                k += 1
                nums1[k] = nums2[j]
                j += 1
                k += 1
        if i < m + n:
            for r in nums1[i:]:
                nums1[k] = r
                k += 1
        elif j < n:
            for r in nums2[j:]:
                nums1[k] = r
                k += 1
        return nums1
