from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,1,2,2,3,4,2,3], 6, 2], [[6,10,12]]],
        [[[3,8,7,8,7,5], 2, 2], [[11,15,15,15,12]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().findXSum(input[0], input[1], input[2])
        display_io(
            input=f"nums = {input[0]}, k = {input[1]}, x = {input[2]}",
            output=ret,
        )

        assert ret == expected_output[0]
