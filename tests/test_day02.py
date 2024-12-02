from pathlib import Path

import pytest

from solutions.day02 import check_report, check_report_with_dampener
from tests.utils import (
    assert_solution_part_returns_expected,
    assert_solution_part_returns_expected_on_path,
)


@pytest.mark.parametrize(
    ("report", "safe"),
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_check_report(report: list[int], safe: bool) -> None:
    assert check_report(report) == safe


@pytest.mark.parametrize(
    ("report", "safe"),
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_report_level_with_dampener(report: list[int], safe: bool) -> None:
    assert check_report_with_dampener(report) == safe


def test_part_1_example() -> None:
    test_data = Path("tests/inputs/02.txt")
    assert_solution_part_returns_expected_on_path(test_data, 2, 1, 2)


def test_part_2_example() -> None:
    test_data = Path("tests/inputs/02.txt")
    assert_solution_part_returns_expected_on_path(test_data, 2, 2, 4)


def test_part_1() -> None:
    assert_solution_part_returns_expected(2, 1, 230)


def test_part_2() -> None:
    pass
