
from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
    ]

    for params in inputs:
        ret = approach.Solution().longestCommonPrefix(params[0])
        display_io(
            input=f"strs = {params[0]}",
            output=ret,
        )
