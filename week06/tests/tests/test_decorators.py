from unittest.mock import patch

import pytest

from custom_decorators import calculate_total, execution_time, logger


@pytest.fixture
def sample_numbers() -> list[int]:
    return [10, 20, 30, 40]


def test_calculate_total(sample_numbers: list[int]) -> None:
    result = calculate_total(sample_numbers)

    assert result == 100


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 6),
        ([10, 20], 30),
        ([5], 5),
        ([], 0),
    ],
)
def test_calculate_total_parametrized(
    numbers: list[int],
    expected: int,
) -> None:
    assert calculate_total(numbers) == expected


def test_logger_output(sample_numbers: list[int]) -> None:
    with patch("builtins.print") as mock_print:
        result = calculate_total(sample_numbers)

    assert result == 100

    assert mock_print.call_count >= 2

    mock_print.assert_any_call("Executing calculate_total")
    mock_print.assert_any_call("Execution completed")


def test_execution_time() -> None:
    @execution_time
    def sample_function() -> int:
        return 42

    with patch("builtins.print") as mock_print:
        result = sample_function()

    assert result == 42
    mock_print.assert_called_once()


def test_logger_preserves_function_metadata() -> None:
    assert calculate_total.__name__ == "calculate_total"