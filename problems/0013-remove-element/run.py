from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[3,2,2,3], 3], [len([2,2])]],
        [[[0,1,2,2,3,0,4,2], 2], [len([0,1,4,0,3])]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().removeElement(nums=input[0], val=input[1])
        display_io(
            input=f"nums = {input[0]}, val = {input[1]}",
            output=ret,
        )
        assert ret == expected_output[0]
