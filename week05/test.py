import asyncio

from toy_event_loop import EventLoop, worker
from concurrency_benchmark import (
    sequential_io,
    threading_benchmark,
    multiprocessing_benchmark,
    asyncio_benchmark,
)


def test_toy_event_loop():

    print("=" * 50)
    print("Testing Toy Event Loop")
    print("=" * 50)

    loop = EventLoop()

    loop.create_task(worker("Task 1", 1))
    loop.create_task(worker("Task 2", 2))

    loop.run_forever()

    print("✓ Toy Event Loop Test Passed\n")


def test_io_benchmarks():

    print("=" * 50)
    print("Testing I/O Benchmarks")
    print("=" * 50)

    sequential_io()
    threading_benchmark()
    asyncio.run(asyncio_benchmark())

    print("✓ I/O Benchmark Test Passed\n")


def test_cpu_benchmark():

    print("=" * 50)
    print("Testing CPU Benchmark")
    print("=" * 50)

    multiprocessing_benchmark()

    print("✓ CPU Benchmark Test Passed\n")


if __name__ == "__main__":

    test_toy_event_loop()
    test_io_benchmarks()
    test_cpu_benchmark()

    print("=" * 50)
    print("All Tests Passed Successfully")
    print("=" * 50)