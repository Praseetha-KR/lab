from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["egg", "add"], [True]],
        [["foo", "bar"], [False]],
        [["paper", "title"], [True]],
        [["badc", "baba"], [False]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().isIsomorphic(input[0], input[1])
        display_io(
            input=f"s = {input[0]}, t = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
