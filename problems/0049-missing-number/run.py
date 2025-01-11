from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[3,0,1]], [2]],
        [[[0,1]], [2]],
        [[[9,6,4,2,3,5,7,0,1]], [8]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().missingNumber(input[0])
        display_io(
            input=f"i = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
