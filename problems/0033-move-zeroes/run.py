from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[0,1,0,3,12]], [[1,3,12,0,0]]],
        [[[0]], [[0]]],
        [[[0,1,9,0,0,3,12,0]], [[1,9,3,12,0,0,0,0]]],
        [[[2,1]], [[2,1]]],
        [[[1,0,1]], [[1,1,0]]],
    ]

    for input, expected_output in test_cases:
        nums = input[0]
        approach.Solution().moveZeroes(nums)
        display_io(
            input=f"nums = {input[0]}",
            output=nums,
        )

        assert nums == expected_output[0]
