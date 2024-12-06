import time
from datetime import timedelta
from copy import deepcopy


def main():

    with open("day_02/data.txt") as f:
        numbers = [[int(n) for n in line.split()] for line in f]

    safe_reports = 0
    for set_of_numbers in numbers:

        if verify_validity(set_of_numbers):
            safe_reports += 1
        else:
            for i in range(len(set_of_numbers)):
                edited_differences = set_of_numbers[:i] + set_of_numbers[i + 1 :]
                if verify_validity(edited_differences):
                    safe_reports += 1
                    break

    print(safe_reports)


def verify_validity(set_of_numbers):
    differences = [
        set_of_numbers[i] - set_of_numbers[i + 1]
        for i in range(len(set_of_numbers) - 1)
    ]

    if all(x > 0 and x <= 3 for x in differences) or all(
        x < 0 and x >= -3 for x in differences
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
