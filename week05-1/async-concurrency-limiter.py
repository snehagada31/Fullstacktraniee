import asyncio


async def worker(task_id, delay, semaphore, should_fail=False):
    async with semaphore:
        print(f"Task {task_id} started")

        await asyncio.sleep(delay)

        if should_fail:
            raise ValueError(f"Task {task_id} failed")

        print(f"Task {task_id} completed")

        return f"Result from Task {task_id}"


async def run_tasks(task_count, concurrency_limit):
    semaphore = asyncio.Semaphore(concurrency_limit)

    tasks = []

    for task_id in range(1, task_count + 1):
        delay = 1

        should_fail = task_id == 4

        task = worker(
            task_id,
            delay,
            semaphore,
            should_fail
        )

        tasks.append(task)

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    return results


async def main():

    print("=" * 50)
    print("Async Concurrency Limiter")
    print("=" * 50)

    results = await run_tasks(
        task_count=6,
        concurrency_limit=2
    )

    print("\nResults:")
    print("-" * 50)

    for index, result in enumerate(results, start=1):

        if isinstance(result, Exception):
            print(f"Task {index}: ERROR - {result}")

        else:
            print(f"Task {index}: {result}")


if __name__ == "__main__":
    asyncio.run(main())