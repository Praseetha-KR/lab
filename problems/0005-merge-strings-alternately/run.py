
from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        [
            "abc",
            "pqr"
        ],
        [
            "ab",
            "pqrs"
        ],
        [
            "abcd",
            "pq"
        ],
        [
            "gmumn",
            "azia"
        ],
        [
            "",
            "ab"
        ],
        [
            "",
            ""
        ]
    ]

    for params in inputs:
        ret = approach.Solution().mergeAlternately(params[0], params[1])
        display_io(
            input=f"word1 = {params[0]}, word2 = {params[1]}",
            output=ret,
        )
