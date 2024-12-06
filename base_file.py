import time
from datetime import timedelta


def main():
    with open("day_XXXXXX/data.txt") as f:
        for line in f.readlines():
            pass


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
