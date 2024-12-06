from dataclasses import dataclass
from typing import List, Set, Tuple, Dict, Optional
import time
from datetime import timedelta


@dataclass
class Position:
    row: int
    col: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.row + other.row, self.col + other.col)

    def is_valid(self, grid: List[List[str]]) -> bool:
        return 0 <= self.row < len(grid) and 0 <= self.col < len(grid[0])


class Guard:
    DIRECTIONS: Dict[str, Position] = {
        "^": Position(-1, 0),
        ">": Position(0, 1),
        "v": Position(1, 0),
        "<": Position(0, -1),
    }

    ROTATION = {"^": ">", ">": "v", "v": "<", "<": "^"}

    def __init__(self, symbol: str, pos: Position):
        self.symbol = symbol
        self.pos = pos

    def move(self, grid: List[List[str]]) -> bool:
        next_pos = self.pos + self.DIRECTIONS[self.symbol]

        if not next_pos.is_valid(grid):
            return False

        if grid[next_pos.row][next_pos.col] == ".":
            grid[self.pos.row][self.pos.col] = "."
            grid[next_pos.row][next_pos.col] = self.symbol
            self.pos = next_pos
        else:
            self.symbol = self.ROTATION[self.symbol]
            grid[self.pos.row][self.pos.col] = self.symbol

        return True


def find_guard(grid: List[List[str]]) -> Optional[Guard]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in Guard.DIRECTIONS:
                return Guard(grid[row][col], Position(row, col))
    return None


def simulate_guard_path(grid: List[List[str]]) -> Set[Tuple[int, int]]:
    visited = set()
    guard = find_guard(grid)

    while guard:
        visited.add((guard.pos.row, guard.pos.col))
        if not guard.move(grid):
            break

    return visited


def main():
    start_time = time.perf_counter()

    with open("day_06/data.txt") as f:
        grid = [list(line.strip()) for line in f]

    visited = simulate_guard_path(grid)
    print(f"Visited squares: {len(visited)}")

    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")


if __name__ == "__main__":
    main()
