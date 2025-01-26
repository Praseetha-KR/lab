import heapq
from typing import List


class KthLargest:
    # Time Complexity: O((M+N)⋅logk)
    # Space Complexity: O(k)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
