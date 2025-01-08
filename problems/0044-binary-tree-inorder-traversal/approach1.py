from typing import List, Optional

from .base import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node: Optional[TreeNode], res: List[int] = []):
        if node is not None:
            self.inorder(node.left, res)
            res.append(node.val)
            self.inorder(node.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res
