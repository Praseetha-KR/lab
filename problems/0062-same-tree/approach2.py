from collections import deque
from typing import Optional

from .base import TreeNode


class Solution:
    # Iteration using deque
    # Time complexity : O(N)
    # Space complexity : O(N)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check_pair(p:  Optional[TreeNode], q:  Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if check_pair(p, q) is False:
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True
