import re
import time
from datetime import timedelta


def main():
    with open("day_07/data.txt", "r") as f:
        data = [
            list(map(int, re.split(r": | ", line.strip()))) for line in f.readlines()
        ]

        print(sum(parse_data(d) for d in data))


def parse_data(d):
    expected = d[0]
    start_number = d[1]
    remainder_numbers = d[2:]
    if recursion(expected, start_number, remainder_numbers):
        return expected
    else:
        return 0


def recursion(expected, current, numbers):
    if len(numbers) == 0:
        return expected == current
    if current > expected:
        return False
    nxt = numbers[0]
    remainder = numbers[1:]
    return (
        recursion(expected, int(f"{current}{nxt}"), remainder)
        or recursion(expected, current + nxt, remainder)
        or recursion(expected, current * nxt, remainder)
    )


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
