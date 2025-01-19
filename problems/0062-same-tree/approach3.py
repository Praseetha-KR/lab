from typing import Optional

from .base import TreeNode


class Solution:
    # Iteration using queue
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

        queue = [(p, q)]
        while len(queue):
            p, q = queue.pop(0)
            if check_pair(p, q) is False:
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True
