from functools import wraps
import time
from typing import Any, Callable, TypeVar, ParamSpec



P = ParamSpec("P") 

R = TypeVar("R")


def logger(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator to log function execution.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Executing {func.__name__}")

        result = func(*args, **kwargs)

        print("Execution completed")

        return result

    return wrapper


def execution_time(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator to calculate execution time.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"Execution time: {end - start:.6f} seconds"
        )

        return result

    return wrapper


@logger
@execution_time
def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]

    result = calculate_total(numbers)

    print("Total:", result)