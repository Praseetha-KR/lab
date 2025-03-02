import os
import sys

from termcolor import colored

LEETCODE_PROBLEM_URL = "https://leetcode.com/problems/{}"

RUN_PY_TPL = """from types import FunctionType, ModuleType


def run(approach: ModuleType, display_io: FunctionType) -> None:
    test_cases = [
        [[], []],
    ]

    for input, expected_output in test_cases:
        ret = approach.Solution().fn(input[0])
        display_io(
            input=f"i = {input[0]}",
            output=ret,
        )

        assert ret == expected_output[0]
"""

def get_dir_tree(dir: str) -> None:
    dir_tree = ""
    indent = 0
    spacer = ' ' * 3

    path_items = dir.split("/")
    for i, item in enumerate(path_items):
        dir_tree += f"\n{spacer * i}{item}/"
        indent = i

    items = os.listdir(dir)
    for item in items[:-1]:
        dir_tree += f"\n{spacer * indent} ├── {item}"
    dir_tree += f"\n{spacer * indent} └── {items[-1]}"
    return dir_tree


def generate_problem_dir(problem_name: str, problem_number: str):
    try:
        problem_dir = f"problems/{problem_number}-{problem_name}"

        os.mkdir(problem_dir)
        print(colored(f"Created problem directory: {problem_dir}", "green"))

        with open(f"{problem_dir}/problem_statement.txt", "w") as fd:
            fd.write(LEETCODE_PROBLEM_URL.format(problem_name))

        with open(f"{problem_dir}/approach1.py", "w"):
            pass

        with open(f"{problem_dir}/run.py", "w") as fd:
            fd.write(RUN_PY_TPL)

        print(colored(get_dir_tree(problem_dir)))

    except Exception as e:
        print(colored(f"Error: {str(e)}", "red"))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            colored(
                "Usage: python problems/generate.py <problem-name> <problem-number>",
                "red"
            )
        )
        sys.exit(1)
    generate_problem_dir(sys.argv[1], sys.argv[2])
