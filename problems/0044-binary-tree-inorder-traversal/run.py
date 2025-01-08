from types import FunctionType, ModuleType

from .base import Tree


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,None,2,3]], [[1,3,2]]],
        [[[1,2,3,4,5,None,8,None,None,6,7,9]], [[4,2,6,5,7,1,3,9,8]]],
        [[[]], [[]]],
        [[[1]], [[1]]],
    ]

    for input, expected_output in test_cases:
        tree= Tree.from_list(input[0])
        ret = approach.Solution().inorderTraversal(tree)
        display_io(
            input=f"root = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
