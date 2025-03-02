from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [["aA", "aAAbbbb"], [3]],
        [["z", "ZZ"], [0]],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().numJewelsInStones(input[0], input[1])
        display_io(
            input=f"jewels = {input[0]} stones = {input[1]}",
            output=ret,
        )

        assert ret == expected_output[0]
