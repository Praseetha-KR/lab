from types import ModuleType, FunctionType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    inputs = [
        [
            [1,2,3,0,0,0],
            3,
            [2,5,6],
            3,
        ],
        [
            [1],
            1,
            [],
            0,
        ],
        [
            [0],
            0,
            [1],
            1,
        ]
    ]

    for params in inputs:
        ret = approach.Solution().merge(params[0], params[1], params[2], params[3])
        display_io(
            input=f"nums1 = {params[0]}, m = {params[1]}, nums2 = {params[2]}, n = {params[3]}",
            output=ret,
        )
