from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[10,2,5,3]], [True]],
        [[[3,1,7,11]], [False]],
        [[[7,1,14,11]], [True]],
        [[[2,3,3,0,0], [True]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().checkIfExist(input[0])
        display_io(
            input=f"arr = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
