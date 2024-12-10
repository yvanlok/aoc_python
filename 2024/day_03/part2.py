import time
from datetime import timedelta
import re


def main():
    with open("day_03/data.txt") as f:
        data = "".join(f.readlines())

    total = 0

    do = True

    combined_regex = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

    matches = re.findall(combined_regex, data)

    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do == True:
            num1, num2 = match.split(",")
            total += int(num1[4:]) * int(num2[:-1])

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
