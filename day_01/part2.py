import time
from datetime import timedelta


def main():
    with open("day_01/data.txt") as f:
        numbers = [list(map(int, line.strip().split())) for line in f]

    list1, list2 = zip(*numbers)
    list1 = sorted(list1)
    list2 = sorted(list2)

    total_diff = sum(abs(a - b) for a, b in zip(list1, list2))
    print(total_diff)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
