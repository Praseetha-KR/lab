from types import FunctionType, ModuleType

from .base import LinkedList


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[3,2,0,-4]], 1, [True]],
        [[[1,2]], 0, [True]],
        [[[1]], -1, [False]],
        [[[-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]], -1, [False]],  # noqa: E501
    ]

    for input, pos, expected_output in test_cases:
        input_ll = LinkedList.from_list_with_back_link(input[0], pos)
        ret = approach.Solution().hasCycle(head=input_ll)

        display_io(
            input=f"head = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
