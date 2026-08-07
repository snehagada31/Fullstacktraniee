import asyncio
import threading
import multiprocessing
import time


# -----------------------------
# IO Bound Task
# -----------------------------

def io_task():
    time.sleep(1)


async def async_io_task():
    await asyncio.sleep(1)


# -----------------------------
# CPU Bound Task
# -----------------------------

def cpu_task():

    total = 0

    for i in range(10_000_000):
        total += i * i

    return total


# -----------------------------
# Threading Benchmark
# -----------------------------

def threading_benchmark():

    threads = []

    start = time.perf_counter()

    for _ in range(5):

        t = threading.Thread(target=io_task)

        threads.append(t)

        t.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()

    print(f"Threading (I/O)        : {end-start:.2f} seconds")


# -----------------------------
# Multiprocessing Benchmark
# -----------------------------

def multiprocessing_benchmark():

    processes = []

    start = time.perf_counter()

    for _ in range(5):

        p = multiprocessing.Process(target=cpu_task)

        processes.append(p)

        p.start()

    for process in processes:
        process.join()

    end = time.perf_counter()

    print(f"Multiprocessing (CPU)  : {end-start:.2f} seconds")


# -----------------------------
# Asyncio Benchmark
# -----------------------------

async def asyncio_benchmark():

    start = time.perf_counter()

    tasks = [asyncio.create_task(async_io_task()) for _ in range(5)]

    await asyncio.gather(*tasks)

    end = time.perf_counter()

    print(f"Asyncio (I/O)          : {end-start:.2f} seconds")


# -----------------------------
# Sequential Benchmark
# -----------------------------

def sequential_io():

    start = time.perf_counter()

    for _ in range(5):
        io_task()

    end = time.perf_counter()

    print(f"Sequential (I/O)       : {end-start:.2f} seconds")


def sequential_cpu():

    start = time.perf_counter()

    for _ in range(5):
        cpu_task()

    end = time.perf_counter()

    print(f"Sequential (CPU)       : {end-start:.2f} seconds")


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("I/O Bound Benchmark")
    print("=" * 50)

    sequential_io()
    threading_benchmark()
    asyncio.run(asyncio_benchmark())

    print()

    print("=" * 50)
    print("CPU Bound Benchmark")
    print("=" * 50)

    sequential_cpu()
    multiprocessing_benchmark()

    print()

    print("Results")
    print("-" * 50)
    print("• Threading improves I/O-bound tasks because threads wait while I/O is performed.")
    print("• Asyncio performs very well for large numbers of I/O-bound operations.")
    print("• Multiprocessing performs best for CPU-bound tasks because each process has its own Python interpreter and bypasses the GIL.")
    print("• Threading is not ideal for CPU-bound tasks due to the Global Interpreter Lock (GIL).")