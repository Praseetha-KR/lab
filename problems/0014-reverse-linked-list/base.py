from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    @staticmethod
    def from_list(arr: List[int]) -> Optional[ListNode]:
        next = None
        for a in reversed(arr):
            next = ListNode(val=a, next=next)
        return next

    @staticmethod
    def to_list(head: Optional[ListNode]) -> List[int]:
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res
