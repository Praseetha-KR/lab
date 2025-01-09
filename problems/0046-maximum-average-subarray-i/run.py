from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,12,-5,-6,50,3], 4], [12.75000]],
        [[[5], 1], [5.00000]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().findMaxAverage(input[0], input[1])
        display_io(
            input=f"nums = {input[0]}, k = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
