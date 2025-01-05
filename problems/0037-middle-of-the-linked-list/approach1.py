import math
from typing import Optional

from .base import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        full_counter = 1
        ptr = head
        while ptr:
            ptr = ptr.next
            full_counter += 1

        mid = math.ceil(full_counter / 2)
        half_counter = 1
        while half_counter < mid:
            head = head.next
            half_counter += 1
        return head
