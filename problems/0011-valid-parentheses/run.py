from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        ["()"],
        ["()[]{}"],
        ["(]"],
        ["([])"],
        ["]"],
        ["]})"],
    ]

    for params in inputs:
        ret = approach.Solution().isValid(params[0])
        display_io(
            input=f"i = {params[0]}",
            output=ret,
        )
