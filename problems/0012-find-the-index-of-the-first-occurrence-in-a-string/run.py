from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["sadbutsad", "sad"], [0]],
        [["leetcode", "leeto"], [-1]],
        [["hello", "ll"], [2]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().strStr(input[0], input[1])
        display_io(
            input=f"haystack = {input[0]}, needle = {input[1]}",
            output=ret,
        )
        assert ret == expected_output[0]
