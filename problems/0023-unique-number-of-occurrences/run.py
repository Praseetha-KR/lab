from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,2,1,1,3]], [True]],
        [[[1,2]], [False]],
        [[[-3,0,1,-3,1,1,1,-3,10,0]], [True]],
        [[[-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]], [True]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().uniqueOccurrences(input[0])
        display_io(
            input=f"arr = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
