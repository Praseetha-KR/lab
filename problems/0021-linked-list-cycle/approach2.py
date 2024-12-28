from typing import Optional

from .base import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using Floyd's cycle finding algorithm
        if head is None:
            return False
        tortoise = head
        hare = head.next
        while tortoise != hare:
            if hare is None or hare.next is None:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True
