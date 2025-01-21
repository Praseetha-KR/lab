from typing import Optional

from .base import ListNode


class Solution:
    # Hash table
    # Time complexity : O(N+M)
    # Space complexity : O(M)
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        b_nodes = set()
        while headB is not None:
            b_nodes.add(headB)
            headB = headB.next

        while headA is not None:
            if headA in b_nodes:
                return headA
            headA = headA.next

        return None
