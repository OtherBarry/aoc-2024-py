from solutions.base import BaseSolution

DIRECTIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
SEARCH_VALUE = "XMAS"
VALID_X_MAS_BARS = ("SAM", "MAS")
X_MAS_CENTER = "A"

Coordinate = tuple[int, int]


class Solution(BaseSolution):
    def setup(self) -> None:
        self.grid = list(self.raw_input.splitlines())
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def is_in_bounds(self, y: int, x: int) -> bool:
        return 0 <= y < self.height and 0 <= x < self.width

    def is_search_value_in_direction(
        self, start: Coordinate, direction: Coordinate
    ) -> bool:
        y, x = start
        dy, dx = direction
        for character in SEARCH_VALUE:
            if not self.is_in_bounds(y, x):
                return False
            if self.grid[y][x] != character:
                return False
            y += dy
            x += dx
        return True

    def is_center_of_x_mas(self, start: Coordinate) -> bool:
        y, x = start
        top_left = self.grid[y + 1][x - 1] + X_MAS_CENTER + self.grid[y - 1][x + 1]
        bottom_left = self.grid[y - 1][x - 1] + X_MAS_CENTER + self.grid[y + 1][x + 1]
        return top_left in VALID_X_MAS_BARS and bottom_left in VALID_X_MAS_BARS

    def part_1(self) -> int:
        found_words = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == SEARCH_VALUE[0]:
                    found_words += sum(
                        self.is_search_value_in_direction((y, x), direction)
                        for direction in DIRECTIONS
                    )
        return found_words

    def part_2(self) -> int:
        found_x_mas = 0
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if self.grid[y][x] == X_MAS_CENTER:
                    found_x_mas += int(self.is_center_of_x_mas((y, x)))
        return found_x_mas
