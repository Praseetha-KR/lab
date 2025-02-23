from types import FunctionType, ModuleType

from .base import Tree


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[3,9,20,None,None,15,7]], [True]],
        [[[1,2,2,3,3,None,None,4,4]], [False]],
        [[[]], [True]],
    ]

    for input, expected_output in test_cases:
        tree= Tree.from_list(input[0])
        ret = approach.Solution().isBalanced(tree)
        display_io(
            input=f"root = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
