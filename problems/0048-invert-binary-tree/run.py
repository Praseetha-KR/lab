from types import FunctionType, ModuleType

from .base import Tree


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[4,2,7,1,3,6,9]], [[4,7,2,9,6,3,1]]],
        [[[2,1,3]], [[2,3,1]]],
        [[[]], [[]]],
    ]

    for input, expected_output in test_cases:
        tree= Tree.from_list(input[0])
        ret_tree = approach.Solution().invertTree(tree)
        ret = Tree.to_list(ret_tree)
        display_io(
            input=f"root = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
