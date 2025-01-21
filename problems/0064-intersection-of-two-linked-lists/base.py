from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return id(self)

    # def __repr__(self):
    #     return f"ListNode(val={self.val})"

class LinkedList:
    @staticmethod
    def from_list(arr: List[int], tail: ListNode = None) -> Optional[ListNode]:
        next = tail
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
