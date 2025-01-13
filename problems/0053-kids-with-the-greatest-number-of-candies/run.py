from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[2,3,5,1,3], 3], [[True,True,True,False,True]]],
        [[[4,2,1,1,2], 1], [[True,False,False,False,False]]],
        [[[12,1,12], 10], [[True,False,True]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().kidsWithCandies(input[0], input[1])
        display_io(
            input=f"candies = {input[0]}, extraCandies = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
