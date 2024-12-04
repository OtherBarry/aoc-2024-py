from collections.abc import Iterator, Sequence
from enum import Enum
from typing import TypeVar

from mypyc.ir.ops import Generic

Coordinate = tuple[int, int]


class Direction(Enum):
    UP = (1, 0)
    DOWN = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (1, -1)
    UP_RIGHT = (1, 1)
    DOWN_LEFT = (-1, -1)
    DOWN_RIGHT = (-1, 1)

    def apply(self, coordinate: Coordinate) -> Coordinate:
        return coordinate[0] + self.value[0], coordinate[1] + self.value[1]


T = TypeVar("T")


class BaseGrid(Generic[T]):
    def __init__(self, grid: Sequence[Sequence[T]]) -> None:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __getitem__(self, coordinate: Coordinate) -> T:
        y, x = coordinate
        return self.grid[y][x]

    def is_in_bounds(self, coordinate: Coordinate) -> bool:
        return 0 <= coordinate[0] < self.height and 0 <= coordinate[1] < self.width

    def get_value(self, coordinate: Coordinate) -> T | None:
        if not self.is_in_bounds(coordinate):
            return None
        return self[coordinate]

    def __iter__(self) -> Iterator[Coordinate]:
        for y in range(self.height):
            for x in range(self.width):
                yield y, x


class CharacterGrid(BaseGrid[str]):
    def __init__(self, raw_input: str) -> None:
        super().__init__(list(raw_input.splitlines()))
