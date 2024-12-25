import time
from datetime import timedelta


def main():
    locks = []
    keys = []
    valid_count = 0

    with open("day_25/data.txt") as f:
        schematics = f.read().strip().split("\n\n")

    for s in schematics:
        s = s.splitlines()
        col_count = [sum(1 for row in s if row[col] == "#") - 1 for col in range(5)]

        if "#" in s[0]:
            locks.append(col_count)
        else:
            keys.append(col_count)

    for key in keys:
        for lock in locks:
            if all(key[col] + lock[col] <= len(key) for col in range(5)):
                valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
