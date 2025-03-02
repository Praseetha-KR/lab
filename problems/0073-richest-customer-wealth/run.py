from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[[[1,2,3],[3,2,1]]], [6]],
        [[[[1,5],[7,3],[3,5]]], [10]],
        [[[[2,8,7],[7,1,3],[1,9,5]]], [17]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().maximumWealth(input[0])
        display_io(
            input=f"accounts = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
