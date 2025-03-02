from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["IceCreAm"], ["AceCreIm"]],
        [["leetcode"], ["leotcede"]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().reverseVowels(input[0])
        display_io(
            input=f"s = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
