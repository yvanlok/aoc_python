import time
from datetime import timedelta


def main():

    values = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    with open("day_01/data.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            digits = []
            for i, c in enumerate(line):
                if c.isnumeric():
                    digits.append(c)
                else:
                    for j in range(len(values)):
                        if line[i:].startswith(values[j]):
                            digits.append(j + 1)
            if digits:
                total += int(str(digits[0]) + str(digits[-1]))
    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
