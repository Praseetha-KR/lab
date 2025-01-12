from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["a", "b"], [False]],
        [["aa", "ab"], [False]],
        [["aa", "aab"], [True]],
        [["bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"], [True]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().canConstruct(input[0], input[1])
        display_io(
            input=f"ransomNote = {input[0]}, magazine = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
