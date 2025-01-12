from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[3,4,5,1,2]], [True]],
        [[[2,1,3,4]], [False]],
        [[[1,2,3]], [True]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().check(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
