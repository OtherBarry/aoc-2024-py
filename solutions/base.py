from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generic, TypeVar

from timer import Timer

T1 = TypeVar("T1")
T2 = TypeVar("T2")


class BaseSolution(ABC, Generic[T1, T2]):
    def __init__(self, input_path: Path) -> None:
        with input_path.open() as f:
            self.raw_input = f.read()

    def setup(self) -> None:
        pass

    @abstractmethod
    def part_1(self) -> T1:
        pass

    @abstractmethod
    def part_2(self) -> T2:
        pass

    def run(self) -> None:
        with Timer() as timer:
            self.setup()
        print(f"\tSetup run in {timer}")
        with Timer() as timer:
            p1_result = self.part_1()
        print(f"\tPart 1 ({timer}): {p1_result}")
        with Timer() as timer:
            p2_result = self.part_2()
        print(f"\tPart 2 ({timer}): {p2_result}")
