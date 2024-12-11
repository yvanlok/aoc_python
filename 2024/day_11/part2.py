import time
from datetime import timedelta
from functools import cache

BLINKS = 75


@cache
def num_splits(stone, blinks):
    length = len(str(stone))

    if blinks == BLINKS:
        return 1

    if stone == 0:
        return num_splits(1, blinks + 1)
    if length % 2 == 0:
        first = int(str(stone)[0 : length // 2])
        second = int(str(stone)[length // 2 :])
        return num_splits(first, blinks + 1) + num_splits(second, blinks + 1)

    return num_splits(stone * 2024, blinks + 1)


def main():
    with open("day_11/data.txt") as f:
        data = tuple(map(int, f.readline().strip().split()))

    total = sum([num_splits(stone, 0) for stone in data])

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
