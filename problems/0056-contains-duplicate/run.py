from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,3,1]], [True]],
        [[[1,2,3,4]], [False]],
        [[[1,1,1,3,3,4,3,2,4,2]], [True]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().containsDuplicate(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
