from types import FunctionType, ModuleType

from .base import LinkedList


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,1,2]], [[1,2]]],
        [[[1,1,2,3,3]], [[1,2,3]]],
    ]

    for input, expected_output in test_cases:
        input_ll1 = LinkedList.from_list(input[0])
        ret_ll = approach.Solution().deleteDuplicates(head=input_ll1)
        ret = LinkedList.to_list(ret_ll)

        display_io(
            input=f"head = {input[0]}",
            output=ret,
        )
        assert ret == expected_output[0]
