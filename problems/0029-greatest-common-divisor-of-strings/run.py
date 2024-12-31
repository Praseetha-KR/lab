from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["ABCABC", "ABC"], ["ABC"]],
        [["ABABAB", "ABAB"], ["AB"]],
        [["LEET", "CODE"], [""]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().gcdOfStrings(input[0], input[1])
        display_io(
            input=f"str1 = {input[0]}, str2 = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
