class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.first = 0
        self.second = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration

        value = self.first
        self.first, self.second = self.second, self.first + self.second
        self.count += 1
        return value


if __name__ == "__main__":
    print("Custom Fibonacci Iterator:")

    fib = FibonacciIterator(10)

    for number in fib:
        print(number, end=" ")
        