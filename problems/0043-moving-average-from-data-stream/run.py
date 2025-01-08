from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [
            [
                ["MovingAverage","next","next","next","next"],
                [[3],[1],[10],[3],[5]]
            ],
            [[None,1.00000,5.50000,4.66667,6.00000]]
        ],
    ]

    for input, expected_output in test_cases:
        methods = input[0]
        params = input[1]
        res = [None]
        obj = getattr(approach, methods[0])(params[0][0])
        for i in range(len(methods) - 1):
            avg = getattr(obj, methods[i + 1])(params[i + 1][0])
            res.append(round(avg, 5))
        ret = res
        display_io(
            input=f"{input[0]}, \n{input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]

# obj = MovingAverage(size)
# param_1 = obj.next(val)
