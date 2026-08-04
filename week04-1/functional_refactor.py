from functools import reduce


def square_numbers(numbers):

    return list(
        map(
            lambda x: x * x,
            numbers
        )
    )



def filter_even_numbers(numbers):

    return list(
        filter(
            lambda x: x % 2 == 0,
            numbers
        )
    )



def calculate_sum(numbers):

    return reduce(
        lambda x, y: x + y,
        numbers
    )



def process_numbers(numbers):

    return {
        "squared": square_numbers(numbers),
        "even": filter_even_numbers(numbers),
        "sum": calculate_sum(numbers)
    }



if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    result = process_numbers(numbers)

    print(result)