from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[2,5,7,8,9,2,3,4,3,1], 3], [True]],
        [[[1,2,3,4,4,4,4,5,6,7], 5], [False]],
        [[[-15,19], 1], [True]],
        [[[-3,-19,-8,-16], 2], [False]],

    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().hasIncreasingSubarrays(input[0], input[1])
        display_io(
            input=f"nums = {input[0]}, k = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
