from typing import Optional

from .base import ListNode


class Solution:
    # Two Pointers
    # Time complexity : O(N+M)
    # Space complexity : O(1)
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA
        return pA
