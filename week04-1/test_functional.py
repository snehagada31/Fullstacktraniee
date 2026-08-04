from functional_refactor import process_numbers


def test_squared_numbers():

    result = process_numbers([1, 2, 3, 4, 5])

    assert result["squared"] == [
        1, 4, 9, 16, 25
    ]


def test_even_numbers():

    result = process_numbers([1, 2, 3, 4, 5])

    assert result["even"] == [
        2, 4
    ]


def test_sum():

    result = process_numbers([1, 2, 3, 4, 5])

    assert result["sum"] == 15