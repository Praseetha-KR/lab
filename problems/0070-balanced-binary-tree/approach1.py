from typing import Optional

from .base import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Top-down recursion
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return True
        return (
            abs(self.height(node.left) - self.height(node.right)) < 2
            and self.is_balanced(node.left)
            and self.is_balanced(node.right)
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced(root)
