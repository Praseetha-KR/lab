from typing import Optional

from .base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Brute Force
    # Time complexity : O(N×M)
    # Space complexity : O(1)
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        while headA is not None:
            hb = headB
            while hb is not None:
                if hb == headA:
                    return headA
                hb = hb.next
            headA = headA.next
        return None
