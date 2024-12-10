import time
from datetime import timedelta


def main():
    with open("day_01/data.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            digits = [c for c in line if c.isnumeric()]
            if digits:
                total += int(digits[0] + digits[-1])
        print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
