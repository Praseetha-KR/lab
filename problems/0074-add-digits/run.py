from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[38], [2]],
        [[0], [0]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().addDigits(input[0])
        display_io(
            input=f"num = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
