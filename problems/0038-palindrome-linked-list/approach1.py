from typing import Optional

from .base import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        s = [slow.val]
        fc, sc = 1, 1

        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            s.append(slow.val)
            sc += 1
            fc += 2

        if fast.next is not None:
            fast = fast.next
            fc += 1

        if fc % 2 != 0:  # for odd number of elements
            s.pop()

        slow = slow.next
        while slow is not None:
            top = s.pop()
            if slow.val != top:
                return False
            slow = slow.next
        return True
