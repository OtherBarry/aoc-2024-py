from pathlib import Path

from tests.utils import (
    assert_solution_part_returns_expected,
    assert_solution_part_returns_expected_on_path,
)


def test_part_1_example() -> None:
    test_data = Path("tests/inputs/01.txt")
    assert_solution_part_returns_expected_on_path(test_data, 1, 1, 11)


def test_part_2_example() -> None:
    test_data = Path("tests/inputs/01.txt")
    assert_solution_part_returns_expected_on_path(test_data, 1, 2, 31)


def test_part_1() -> None:
    assert_solution_part_returns_expected(1, 1, 2815556)


def test_part_2() -> None:
    assert_solution_part_returns_expected(1, 2, 23927637)
