from typing import Optional, Tuple

from .base import TreeNode


class Solution:
    def is_balanced_subtree(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        # Bottom-up recursion
        # Time complexity: O(n)
        # Space complexity: O(n)

        if node is None:
            return True, -1
        left_is_balanced, left_height = self.is_balanced_subtree(node.left)
        if not left_is_balanced:
            return False, 0

        right_is_balanced, right_height = self.is_balanced_subtree(node.right)
        if not right_is_balanced:
            return False, 0

        return (
            abs(left_height - right_height) < 2,
            1 + max(left_height, right_height)
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced_subtree(root)[0]
