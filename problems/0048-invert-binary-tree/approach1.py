from typing import Optional

from .base import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap_children(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return
        temp = self.swap_children(node.left)
        node.left = self.swap_children(node.right)
        node.right = temp
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.swap_children(root)
