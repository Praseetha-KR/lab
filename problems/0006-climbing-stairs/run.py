
from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        [2],
        [3],
        [10],
    ]

    for params in inputs:
        ret = approach.Solution().climbStairs(params[0])
        display_io(
            input=f"n = {params[0]}",
            output=ret,
        )
