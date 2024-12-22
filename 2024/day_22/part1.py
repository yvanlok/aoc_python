import time
from datetime import timedelta
from functools import cache
import sys


@cache
def calculate_chunk(num, iterations=100):
    if iterations == 0:
        return num

    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216

    return calculate_chunk(num, iterations - 1)


def calculate_secret_nums(initial_num, step=2000):
    chunks = 20
    num = initial_num
    for i in range(chunks):
        num = calculate_chunk(num)
    return num


def main():
    with open("day_22/data.txt") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    total = 0
    for num in numbers:
        result = calculate_secret_nums(num)
        total += result

    print(f"Total: {total}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
