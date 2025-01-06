from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[3,3,3]], ["equilateral"]],
        [[[3,4,5]], ["scalene"]],
        [[[8,4,2]], ["none"]],
        [[[5,3,8]], ["none"]],
        [[[5,3,5]], ["isosceles"]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().triangleType(input[0])
        display_io(
            input=f"nums = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
