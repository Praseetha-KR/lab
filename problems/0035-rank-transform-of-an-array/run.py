from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[40,10,20,30]], [[4,1,2,3]]],
        [[[100,100,100]], [[1,1,1]]],
        [[[37,12,28,9,100,56,80,5,12]], [[5,3,4,2,8,6,7,1,3]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().arrayRankTransform(input[0])
        display_io(
            input=f"arr = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
