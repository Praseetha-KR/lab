from typing import Optional

from .base import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linked_list_to_integer(self, ll: Optional[ListNode]) -> int:
        num = 0
        i = 0
        while ll is not None:
            num += (10 ** i) * ll.val
            ll = ll.next
            i += 1
        return num

    def integer_to_linked_list(self, n: int) -> Optional[ListNode]:
        if n == 0:
            return ListNode(val=0, next=None)

        res = None
        stack = []
        while n > 0:
            last_digit = n % 10
            stack.append(last_digit)
            n //= 10
        while stack:
            current = ListNode(val=stack.pop(), next=res)
            res = current
        return res

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = self.linked_list_to_integer(l1)
        n2 = self.linked_list_to_integer(l2)
        n = n1 + n2
        return self.integer_to_linked_list(n)
