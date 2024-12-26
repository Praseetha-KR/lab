from typing import Optional

from .base import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using Floyd's Cycle Finding Algorithm
        if head is None:
            return None
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
