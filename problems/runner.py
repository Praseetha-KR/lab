import importlib
import os
import sys
from measure_performance import measure_performance


@measure_performance
def runner(problem_run_module, approach_module):
    problem_run_module.run(approach_module)

if __name__ == "__main__":
    if len(sys.argv)!= 3:
        raise Exception("Missing parameters: problem directory name or approach number")

    problem_run_module = importlib.import_module(f"{sys.argv[1]}.run")
    approach_module = importlib.import_module(f"{sys.argv[1]}.approach{sys.argv[2]}")

    runner(problem_run_module, approach_module)
