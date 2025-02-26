from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[0,1,3,50,75], 0, 99], [[[2,2],[4,49],[51,74],[76,99]]]],
        [[[-1], -1, -1], [[]]],
        [[[], 1, 1], [[[1,1]]]],
        [[[1000000000], 0, 1000000000], [[[0,999999999]]]]
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().findMissingRanges(input[0], input[1], input[2])
        display_io(
            input=f"nums = {input[0]}, lower = {input[1]}, upper = {input[2]}",
            output=ret,
        )

        assert ret == expected_output[0]
