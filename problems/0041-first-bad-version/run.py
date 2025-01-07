from types import FunctionType, ModuleType

from .base import set_bad_version


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[5], [4]],
        [[1], [1]],
        [[2], [2]],
        [[2126753390], [1702766719]],
    ]

    for input, expected_output in test_cases:
        approach.isBadVersion = set_bad_version(expected_output[0])

        ret = approach.Solution().firstBadVersion(input[0])
        display_io(
            input=f"n = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
