from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[1,2,3]], [[1,2,4]]],
        [[[4,3,2,1]], [[4,3,2,2]]],
        [[[9]], [[1,0]]],
        [[[9,9]], [[1,0,0]]],
        [[[9,9,9,9,9]], [[1,0,0,0,0,0]]],
        [[[3, 9, 4, 9, 9, 0, 2, 1, 9]], [[3,9,4,9,9,0,2,2,0]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().plusOne(input[0])
        display_io(
            input=f"digits = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
