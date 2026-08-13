from functools import reduce
from typing import TypedDict


class ProcessedNumbers(TypedDict):
    squared: list[int]
    even: list[int]
    sum: int


def square_numbers(numbers: list[int]) -> list[int]:
    return list(
        map(
            lambda x: x * x,
            numbers
        )
    )


def filter_even_numbers(numbers: list[int]) -> list[int]:
    return list(
        filter(
            lambda x: x % 2 == 0,
            numbers
        )
    )


def calculate_sum(numbers: list[int]) -> int:
    return reduce(
        lambda x, y: x + y,
        numbers
    )


def process_numbers(numbers: list[int]) -> ProcessedNumbers:
    return {
        "squared": square_numbers(numbers),
        "even": filter_even_numbers(numbers),
        "sum": calculate_sum(numbers)
    }


if __name__ == "__main__":
    numbers: list[int] = [1, 2, 3, 4, 5]

    result: ProcessedNumbers = process_numbers(numbers)

    print(result)