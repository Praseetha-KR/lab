from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[], []],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().fn(input[0])
        display_io(
            input=f"i = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
