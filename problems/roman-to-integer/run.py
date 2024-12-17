from types import ModuleType, FunctionType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        ["III"],
        ["LVIII"],
        ["MCMXCIV"],
        ["D"],
    ]

    for params in inputs:
        ret = approach.Solution().romanToInt(params[0])
        display_io(
            input=f"s = {params[0]}",
            output=ret,
        )
