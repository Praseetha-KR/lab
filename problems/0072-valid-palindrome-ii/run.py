from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["aba"], [True]],
        [["abca"], [True]],
        [["abc"], [False]],
        [["deeee"], [True]],
        [["zryxeededexyz"], [False]],
        [["aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"], [True]],  # noqa
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().validPalindrome(input[0])
        display_io(
            input=f"s = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
