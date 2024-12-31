from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["A man, a plan, a canal: Panama"], [True]],
        [["race a car"], [False]],
        [[" "], [True]],
        [["0P"], [False]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().isPalindrome(input[0])
        display_io(
            input=f"s = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
