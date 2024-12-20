from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        ["sadbutsad", "sad"],
        ["leetcode", "leeto"],
        ["hello", "ll"]
    ]

    for params in inputs:
        ret = approach.Solution().strStr(params[0], params[1])
        display_io(
            input=f"haystack = {params[0]}, needle = {params[1]}",
            output=ret,
        )
