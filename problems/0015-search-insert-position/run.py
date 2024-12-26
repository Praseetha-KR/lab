from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,3,5,6], 5], [2]],
        [[[1,3,5,6], 2], [1]],
        [[[1,3,5,6], 7], [4]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().searchInsert(input[0], input[1])
        display_io(
            input=f"nums = {input[0]}, target = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
