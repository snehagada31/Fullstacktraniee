import asyncio


class FakeConnection:

    def __init__(self, connection_id):
        self.connection_id = connection_id

    async def query(self, sql):
        print(
            f"Connection {self.connection_id}: "
            f"executing '{sql}'"
        )

        await asyncio.sleep(1)

        return (
            f"Connection {self.connection_id}: "
            f"query completed"
        )


class AsyncResourcePool:

    def __init__(self, size):
        self.size = size
        self.pool = asyncio.Queue()

    async def initialize(self):

        for connection_id in range(1, self.size + 1):

            connection = FakeConnection(connection_id)

            await self.pool.put(connection)

    async def acquire(self):

        connection = await self.pool.get()

        print(
            f"Connection {connection.connection_id} acquired"
        )

        return connection

    async def release(self, connection):

        print(
            f"Connection {connection.connection_id} released"
        )

        await self.pool.put(connection)

    async def __aenter__(self):

        return self

    async def __aexit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        while not self.pool.empty():
            await self.pool.get()


async def use_connection(pool, task_id):

    connection = await pool.acquire()

    try:

        result = await connection.query(
            f"SELECT * FROM users WHERE id = {task_id}"
        )

        print(f"Task {task_id}: {result}")

    finally:

        await pool.release(connection)


async def main():

    print("=" * 50)
    print("Async Resource Pool")
    print("=" * 50)

    async with AsyncResourcePool(size=2) as pool:

        await pool.initialize()

        tasks = [
            use_connection(pool, task_id)
            for task_id in range(1, 6)
        ]

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())