import time
from datetime import timedelta
import re


def main():
    with open("day_03/data.txt") as f:
        data = "".join(f.readlines())

    total = 0

    multiplications = re.findall(r"mul\(\d+,\d+\)", data)
    for multiplication in multiplications:
        num1, num2 = multiplication.split(",")
        total += int(num1[4:]) * int(num2[:-1])
    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
