from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[4], [2]],
        [[8], [2]],
        [[0], [0]],
        [[2147395599], [46339]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().mySqrt(input[0])
        display_io(
            input=f"x = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
