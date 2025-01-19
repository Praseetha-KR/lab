from types import FunctionType, ModuleType

from .base import Tree


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,3], [1,2,3]], [True]],
        [[[1,2], [1,None,2]], [False]],
        [[[1,2,1], [1,1,2]], [False]],
    ]

    for input, expected_output in test_cases:
        p = Tree.from_list(input[0])
        q = Tree.from_list(input[1])
        ret = approach.Solution().isSameTree(p, q)
        display_io(
            input=f"p = {input[0]}, q = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
