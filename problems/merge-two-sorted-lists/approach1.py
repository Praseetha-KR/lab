from typing import Optional

from .base import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        merged = merged_head = ListNode()
        while list1 and list2:
            if list1.val == list2.val:
                merged.next = list1
                list1, merged = list1.next, merged.next
                merged.next = list2
                list2, merged = list2.next, merged.next
            elif list1.val < list2.val:
                merged.next = list1
                list1, merged = list1.next, merged.next
            else:
                merged.next = list2
                list2, merged = list2.next, merged.next
            if list1 or list2:
                merged.next = list1 if list1 else list2
        return merged_head.next
