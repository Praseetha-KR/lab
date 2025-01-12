from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[4,1,2], [1,3,4,2]], [[-1,3,-1]]],
        [[[2,4], [1,2,3,4]], [[3,-1]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().nextGreaterElement(input[0], input[1])
        display_io(
            input=f"nums1 = {input[0]}, nums2 = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
