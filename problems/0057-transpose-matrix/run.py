from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[[1,2,3],[4,5,6],[7,8,9]]], [[[1,4,7],[2,5,8],[3,6,9]]]],
        [[[[1,2,3],[4,5,6]]], [[[1,4],[2,5],[3,6]]]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().transpose(input[0])
        display_io(
            input=f"matrix = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
