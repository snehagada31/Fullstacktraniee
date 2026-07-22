def fibonacci(limit):

    first = 0
    second = 1

    for _ in range(limit):
        yield first
        first, second = second, first + second


if __name__ == "__main__":

    print("Fibonacci Generator:")

    for number in fibonacci(10):
        print(number, end=" ")

# fruits = ["apple", "mango", "banana"]

# iterator = iter(fruits)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

