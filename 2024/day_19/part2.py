import time
from datetime import timedelta
from functools import lru_cache


@lru_cache(maxsize=None)
def count_combinations(text: str, idx: int, available: tuple[str, ...]) -> int:
    if idx == len(text):
        return 1

    total = 0
    for towel in available:
        if text[idx:].startswith(towel):
            total += count_combinations(text, idx + len(towel), available)
    return total


def main():
    available_towels = []
    total_combinations = 0

    with open("day_19/data.txt") as f:
        available_towels = tuple(f.readline().strip().split(", "))

        for combo in f.readlines()[1:]:
            combo = combo.strip()
            total_combinations += count_combinations(combo, 0, available_towels)

    print(total_combinations)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
