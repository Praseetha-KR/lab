from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["abcde", "cdeab"], [True]],
        [["abcde", "abced"], [False]],
        [["aa", "a"], [False]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().rotateString(input[0], input[1])
        display_io(
            input=f"s = {input[0]}, goal = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
