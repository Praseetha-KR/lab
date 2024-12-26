
from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        [121],
        [-121],
        [10],
    ]

    for params in inputs:
        ret = approach.Solution().isPalindrome(params[0])
        display_io(
            input=f"x = {params[0]}",
            output=ret,
        )
