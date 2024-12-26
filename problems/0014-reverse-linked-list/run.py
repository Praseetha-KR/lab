from types import FunctionType, ModuleType

from .base import LinkedList


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,3,4,5]], [[5,4,3,2,1]]],
        [[[1,2]], [[2,1]]],
        [[[]], [[]]],
    ]

    for input, expected_output in test_cases:
        input_ll = LinkedList.from_list(input[0])
        ret_ll = approach.Solution().reverseList(head=input_ll)
        ret = LinkedList.to_list(ret_ll)

        display_io(
            input=f"head = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
