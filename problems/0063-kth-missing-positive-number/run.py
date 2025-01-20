from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[2,3,4,7,11], 5], [9]],
        [[[1,2,3,4], 2], [6]],
        [[[2], 1], [1]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().findKthPositive(input[0], input[1])
        display_io(
            input=f"arr = {input[0]}, k = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
