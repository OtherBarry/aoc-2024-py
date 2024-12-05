from solutions.base import BaseSolution


class Page:
    def __init__(self, value: int) -> None:
        self.value = value
        self._must_come_before = set[int]()

    def add_rule(self, must_come_before: int) -> None:
        self._must_come_before.add(must_come_before)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Page):
            return NotImplemented
        return other.value in self._must_come_before

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Page):
            return NotImplemented
        return self.value == other.value


def middle_value(values: list[Page]) -> int:
    return values[len(values) // 2].value


class Solution(BaseSolution):
    def setup(self) -> None:
        # Parse input (normal setup)
        raw_rules, raw_updates = self.raw_input.split("\n\n")
        pages = dict[int, Page]()
        for rule_line in raw_rules.splitlines():
            page, before = rule_line.split("|")
            pages.setdefault(int(page), Page(int(page))).add_rule(int(before))
        self.updates = [
            [pages[int(page)] for page in update.split(",")]
            for update in raw_updates.splitlines()
        ]

        # Run logic in setup because it's easier to do both parts at once
        self._part_1_result = 0
        self._part_2_result = 0

        for update in self.updates:
            sorted_update = sorted(update)
            if sorted_update == update:
                self._part_1_result += middle_value(update)
            else:
                self._part_2_result += middle_value(sorted_update)

    def part_1(self) -> int:
        return self._part_1_result

    def part_2(self) -> int:
        return self._part_2_result
