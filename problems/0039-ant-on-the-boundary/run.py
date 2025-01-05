from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[2,3,-5]], [1]],
        [[[3,2,-3,-4]], [0]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().returnToBoundaryCount(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
