from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    @staticmethod
    def from_list_with_back_link(
        arr: List[int], link_back_position: int
    ) -> Optional[ListNode]:
        next = None
        for a in reversed(arr):
            next = ListNode(val=a, next=next)
        head = next

        # link last node back to the specified position creating a cycle
        if link_back_position >= 0:
            node = head
            for i in range(len(arr) - 1):
                if i == link_back_position:
                    pos = node
                node = node.next
            node.next = pos

        return head

