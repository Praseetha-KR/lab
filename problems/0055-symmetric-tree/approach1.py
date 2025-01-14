from typing import Optional

from .base import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_symmetric(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (
            t1.val == t2.val
            and self.is_symmetric(t1.left, t2.right)
            and self.is_symmetric(t1.left, t2.right)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_symmetric(root, root)
