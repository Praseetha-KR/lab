from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        [[3, 2, 3]],
        [[2, 2, 1, 1, 1, 2, 2]],
    ]

    for params in inputs:
        ret = approach.Solution().majorityElement(params[0])
        display_io(
            input=f"nums = {params[0]}",
            output=ret,
        )
