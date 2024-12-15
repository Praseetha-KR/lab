import importlib
import os
import sys
from types import ModuleType
from termcolor import colored
from measure_performance import measure_performance


def display_io(input: str, output: str) -> None:
    print(colored("Input:", "yellow", attrs=["bold"]))
    print(f"{input}\n")
    print(colored("Output:", "green", attrs=["bold"]))
    print(f"{output}\n\n")


@measure_performance
def runner(problem_run_module: ModuleType, approach_module: ModuleType) -> None:
    problem_run_module.run(approach_module, display_io)
    

if __name__ == "__main__":
    if len(sys.argv)!= 3:
        raise Exception("Missing parameters: problem directory name or approach number")

    problem_run_module = importlib.import_module(f"{sys.argv[1]}.run")
    approach_module = importlib.import_module(f"{sys.argv[1]}.approach{sys.argv[2]}")

    runner(problem_run_module, approach_module)
