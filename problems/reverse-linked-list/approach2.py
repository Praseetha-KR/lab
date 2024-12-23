from typing import Optional

from .base import ListNode


class Solution:
    def _reverse(self, head: Optional[ListNode], prev: Optional[ListNode] = None):
        if head is None:
            return prev
        temp = head.next
        head.next = prev
        return self._reverse(temp, head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head)
