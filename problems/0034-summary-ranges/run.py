from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[0,1,2,4,5,7]], [["0->2","4->5","7"]]],
        [[[0,2,3,4,6,8,9]], [["0","2->4","6","8->9"]]],
        [[[]], [[]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().summaryRanges(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
