from typing import Optional

from .base import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
