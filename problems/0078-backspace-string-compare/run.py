from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["ab#c", "ad#c"], [True]],
        [["ab##", "c#d#"], [True]],
        [["a#c", "b"], [False]],
        [["xywrrmp", "xywrrmu#p"], [True]],
        [["a##c", "#a#c"], [True]],
        [["y#fo##f", "y#f#o##f"], [True]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().backspaceCompare(input[0], input[1])
        display_io(
            input=f"s = {input[0]}, t = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
