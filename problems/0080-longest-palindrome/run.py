from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["abccccdd"], [7]],
        [["a"], [1]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().longestPalindrome(input[0])
        display_io(
            input=f"s = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
