from typing import Optional

from .base import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        stack = [slow.val]
        fast_counter = 1
        slow_counter = 1
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            slow_counter += 1
            stack.append(slow.val)
            fast = fast.next.next
            fast_counter += 2

        if fast.next is not None:
            fast = fast.next
            fast_counter += 1

        if (fast_counter/slow_counter) % 2 != 0:
            stack.pop()
        slow = slow.next

        while slow is not None:
            top = stack.pop()
            if slow.val != top:
                return False
            slow = slow.next
        return True
