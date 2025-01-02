from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[-1,0,3,5,9,12], 9], [4]],
        [[[-1,0,3,5,9,12], 2], [-1]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().search(input[0], input[1])
        display_io(
            input=f"nums = {input[0]}, target = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
