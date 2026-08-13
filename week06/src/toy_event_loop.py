import time
from collections import deque
from typing import Generator


class Sleep:

    def __init__(self, delay: float) -> None:
        self.delay: float = delay
        self.wake_time: float = time.perf_counter() + delay


class Task:

    def __init__(self, coroutine: Generator[Sleep, None, None]) -> None:
        self.coroutine = coroutine

    def run(self) -> Sleep:
        return next(self.coroutine)


class EventLoop:

    def __init__(self) -> None:
        self.ready: deque[Task] = deque()
        self.sleeping: list[tuple[Task, Sleep]] = []

    def create_task(self, coroutine: Generator[Sleep, None, None]) -> None:
        self.ready.append(Task(coroutine))

    def run_forever(self) -> None:

        while self.ready or self.sleeping:

            now = time.perf_counter()

            for task, sleep_obj in self.sleeping[:]:
                if now >= sleep_obj.wake_time:
                    self.ready.append(task)
                    self.sleeping.remove((task, sleep_obj))

            if not self.ready:
                time.sleep(0.01)
                continue

            task = self.ready.popleft()

            try:

                result = task.run()

                if isinstance(result, Sleep):
                    self.sleeping.append((task, result))

                else:
                    self.ready.append(task)

            except StopIteration:
                pass


def sleep(seconds: float) -> Generator[Sleep, None, None]:
    yield Sleep(seconds)


def worker(name: str, delay: float) -> Generator[Sleep, None, None]:

    print(f"{name} started")

    yield from sleep(delay)

    print(f"{name} resumed after {delay} second(s)")

    yield from sleep(delay)

    print(f"{name} finished")


if __name__ == "__main__":

    loop = EventLoop()

    loop.create_task(worker("Task A", 2))
    loop.create_task(worker("Task B", 1))
    loop.create_task(worker("Task C", 3))

    start = time.perf_counter()

    loop.run_forever()

    end = time.perf_counter()

    print(f"\nTotal Execution Time : {end - start:.2f} seconds")