from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,1,0,1,1,1]], [3]],
        [[[1,0,1,1,0,1]], [2]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().findMaxConsecutiveOnes(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
