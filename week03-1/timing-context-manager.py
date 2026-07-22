import time
from contextlib import contextmanager


# -------------------------------
# Class-based Context Manager
# -------------------------------

class Timer:

    def __enter__(self):
        self.start = time.perf_counter()
        print("Timer started...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.perf_counter()
        print(f"Execution Time: {end - self.start:.4f} seconds")


# -------------------------------
# Decorator-based Context Manager
# -------------------------------

@contextmanager
def timer():

    start = time.perf_counter()

    print("Timer started...")

    try:
        yield

    finally:
        end = time.perf_counter()
        print(f"Execution Time: {end - start:.4f} seconds")


# -------------------------------
# Testing
# -------------------------------

if __name__ == "__main__":

    print("Class-based Context Manager")

    with Timer():
        time.sleep(2)

    print()

    print("Decorator-based Context Manager")

    with timer():
        time.sleep(2)