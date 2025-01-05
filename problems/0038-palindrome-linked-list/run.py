from types import FunctionType, ModuleType

from .base import LinkedList


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,2,1]], [True]],
        [[[1,2]], [False]],
        [[[1,2,4,2,1]], [True]],
        [[[1,2,4,4,2,1]], [True]],
        [[[1,2,2,1,2,3,4,3,2,1,2,2,1]], [True]],
        [[[1,2,2,1,2,3,3,2,1,2,2,1]], [True]],
        [[[1,1]], [True]],
        [[[1,1,1]], [True]],
    ]

    for input, expected_output in test_cases:
        input_ll1 = LinkedList.from_list(input[0])
        ret = approach.Solution().isPalindrome(head=input_ll1)

        display_io(
            input=f"head = {input[0]}",
            output=ret,
        )
        assert ret == expected_output[0]
