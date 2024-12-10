import time
from datetime import timedelta


def main():
    with open("day_02/data.txt") as f:
        numbers = [[int(n) for n in line.split()] for line in f]

    safe_reports = 0
    for set_of_numbers in numbers:
        differences = [
            set_of_numbers[i] - set_of_numbers[i + 1]
            for i in range(len(set_of_numbers) - 1)
        ]
        if all(0 < x <= 3 for x in differences) or all(
            -3 <= x < 0 for x in differences
        ):
            safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
