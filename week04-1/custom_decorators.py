from functools import wraps
import time


def logger(func):
    """
    Decorator to log function execution
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Executing {func.__name__}")

        result = func(*args, **kwargs)

        print("Execution completed")

        return result

    return wrapper



def execution_time(func):
    """
    Decorator to calculate execution time
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            f"Execution time: {end - start:.6f} seconds"
        )

        return result

    return wrapper



@logger
@execution_time
def calculate_total(numbers):

    return sum(numbers)



if __name__ == "__main__":

    numbers = [10, 20, 30, 40]

    result = calculate_total(numbers)

    print("Total:", result)