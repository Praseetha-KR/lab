from types import FunctionType, ModuleType

from .base import Tree


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,3,4,5]], [3]],
        [[[1,2]], [1]],
    ]

    for input, expected_output in test_cases:
        tree= Tree.from_list(input[0])
        ret = approach.Solution().diameterOfBinaryTree(tree)
        display_io(
            input=f"root = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
