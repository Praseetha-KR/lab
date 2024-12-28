from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[1], [True]],
        [[16], [True]],
        [[3], [False]],
        [[536870912], [True]],
        [[32767], [False]],
        [[536870911], [False]],
        [[0], [False]],
        [[-16], [False]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().isPowerOfTwo(input[0])
        display_io(
            input=f"n = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
