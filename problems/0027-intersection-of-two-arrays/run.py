from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,2,1], [2,2]], [[2]]],
        [[[4,9,5], [9,4,9,8,4]], [[4,9]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().intersection(input[0], input[1])
        display_io(
            input=f"nums1 = {input[0]}, nums2 = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
