import os
import time
from types import FunctionType

import psutil
from termcolor import colored


def measure_performance(func: FunctionType) -> FunctionType:
    def wrapper(*args, **kwargs):
        # Get the process ID
        process = psutil.Process(os.getpid())

        # Measure memory usage before execution
        mem_before = process.memory_info().rss / (1024 * 1024)  # in MB

        # Measure execution time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # Measure memory usage after execution
        mem_after = process.memory_info().rss / (1024 * 1024)  # in MB

        execution_time = end_time - start_time
        memory_usage = mem_after - mem_before

        print(
            colored("Execution time: ", "light_blue"),
            colored(f"{execution_time:.6f} seconds", "light_magenta")
        )
        print(
            colored("Memory usage: ", "light_blue"),
            colored(f"{memory_usage:.6f} MB", "light_magenta")
        )

        return result

    return wrapper
