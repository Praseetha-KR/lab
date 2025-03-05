from types import FunctionType, ModuleType

from .base import LinkedList


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[2,4,3], [5,6,4]], [[7,0,8]]],
        [[[0], [0]], [[0]]],
        [[[9,9,9,9,9,9,9], [9,9,9,9]], [[8,9,9,9,0,0,0,1]]],
    ]

    for input, expected_output in test_cases:
        input_ll1 = LinkedList.from_list(input[0])
        input_ll2 = LinkedList.from_list(input[1])
        ret_ll = approach.Solution().addTwoNumbers(l1=input_ll1, l2=input_ll2)
        ret = LinkedList.to_list(ret_ll)

        display_io(
            input=f"l1 = {input[0]}, l2 = {input[1]}",
            output=ret,
        )
        assert ret == expected_output[0]
