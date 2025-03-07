from typing import Optional

from .base import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current_node = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            col_sum = l1_val + l2_val + carry
            new_node = ListNode(col_sum % 10)
            carry = col_sum // 10
            current_node.next = new_node
            current_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
