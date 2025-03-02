from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[27], [True]],
        [[0], [False]],
        [[-1], [False]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().isPowerOfThree(input[0])
        display_io(
            input=f"n = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
