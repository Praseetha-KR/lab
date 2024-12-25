from types import FunctionType, ModuleType

from .base import LinkedList


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,4], [1,3,4]], [[1,1,2,3,4,4]]],
        [[[], []], [[]]],
        [[[], [0]], [[0]]],
    ]

    for input, expected_output in test_cases:
        input_ll1 = LinkedList.from_list(input[0])
        input_ll2 = LinkedList.from_list(input[1])
        ret_ll = approach.Solution().mergeTwoLists(list1=input_ll1, list2=input_ll2)
        ret = LinkedList.to_list(ret_ll)

        display_io(
            input=f"list1 = {input[0]}, list2 = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
