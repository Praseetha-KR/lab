from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[2,2,1]], [1]],
        [[[4,1,2,1,2]], [4]],
        [[[1]], [1]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().singleNumber(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
