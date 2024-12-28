from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["11", "1"], ["100"]],
        [["1010", "1011"], ["10101"]],
        [["1", "111"], ["1000"]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().addBinary(input[0], input[1])
        display_io(
            input=f"a = {input[0]}, b = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
