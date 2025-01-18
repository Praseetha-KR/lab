from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[2], [1]],
        [[3], [2]],
        [[4], [3]],
        [[6], [8]],
        [[7], [13]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().fib(input[0])
        display_io(
            input=f"n = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
