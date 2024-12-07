from collections.abc import Iterable
from operator import add, mul
from itertools import product
from typing import Callable

from tqdm import tqdm


from solutions.base import BaseSolution

Operator = Callable[[int, int], int]


def combination_can_be_solved(combination: Iterable[Operator], values: list[int], answer: int) -> bool:
    result = values[0]
    for operator, value in zip(combination, values[1:]):
        result = operator(result, value)
        if result > answer:
            return False
    return result == answer


def equation_can_be_solved(operators: Iterable[Operator], values: list[int], answer: int) -> bool:
    for combination in product(operators, repeat=len(values) - 1):
        if combination_can_be_solved(combination, values, answer):
            return True
    return False


def concatenate(a: int, b: int) -> int:
    return int(str(a) + str(b))


class Solution(BaseSolution):
    def setup(self) -> None:
        self.equations = []
        for line in self.raw_input.splitlines():
            raw_answer, raw_values = line.split(":")
            self.equations.append((int(raw_answer), [int(x) for x in raw_values.split()]))


    def part_1(self) -> int:
        operators = (add, mul)
        return sum(
            answer
            for answer, values in self.equations
            if equation_can_be_solved(operators, values, answer)
        )

    def part_2(self) -> int:
        operators = (add, mul, concatenate)
        return sum(
            answer
            for answer, values in self.equations
            if equation_can_be_solved(operators, values, answer)
        )
