from typing import Optional

from .base import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using seen set of nodes
        seen = set()
        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
