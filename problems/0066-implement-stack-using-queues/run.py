from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [
            [
                ["MyStack","push","push","top","pop","empty"],
                [[],[1],[2],[],[],[]]
            ],
            [
                [None,None,None,2,2,False]
            ]
        ],
    ]

    for input, expected_output in test_cases:
        methods = input[0]
        params = input[1]
        res = [None]
        obj = getattr(approach, methods[0])()
        for i in range(len(methods) - 1):
            if len(params[i + 1]):
                method_output = getattr(obj, methods[i + 1])(params[i + 1][0])
                res.append(method_output)
            else:
                method_output = getattr(obj, methods[i + 1])()
                res.append(method_output)
        ret = res
        display_io(
            input=f"{input[0]}, \n{input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
