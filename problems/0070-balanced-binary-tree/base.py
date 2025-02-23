from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    @staticmethod
    def from_list(arr: List[int]) -> Optional[TreeNode]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(val=arr[0])
        queue = [root]
        i = 1

        while queue and i < len(arr):
            node = queue.pop(0)

            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
        return root

    @staticmethod
    def to_list(root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            current = queue.popleft()
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
