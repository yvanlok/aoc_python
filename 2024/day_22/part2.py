import time
from datetime import timedelta
from collections import defaultdict

PRUNE = (2**24) - 1


def secret(num, times=2001):

    digits = [num % 10]
    deltas = []

    for _ in range(times):
        num = ((num << 6) ^ num) & PRUNE
        num = ((num >> 5) ^ num) & PRUNE
        num = ((num << 11) ^ num) & PRUNE

        digit = num % 10
        deltas.append(digit - digits[-1])
        digits.append(digit)

    return num, digits, deltas


def main():
    with open("day_22/data.txt") as f:
        codes = [int(line.strip()) for line in f.readlines()]

    sequences = defaultdict(int)

    for code in codes:
        num, digits, changes = secret(code)

        seen = set()

        for i in range(4, len(changes)):
            seq = tuple(changes[i - 4 : i])

            if seq in seen:
                continue
            sequences[seq] += digits[i]
            seen.add(seq)

    print(max(sequences.values()))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
