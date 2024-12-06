import time
from datetime import timedelta
from functools import cmp_to_key


def compare(x, y, rules):
    return -(x + "|" + y in rules)


def main():
    with open("day_05/data.txt") as f:
        ordering_rules, updates = "".join(f.readlines()).split("\n\n")
        ordering_rules = [line.split("|") for line in ordering_rules.splitlines()]
        updates = [line.split(",") for line in updates.splitlines()]

    rules_set = set("|".join(rule) for rule in ordering_rules)
    cmp = cmp_to_key(lambda x, y: compare(x, y, rules_set))

    total = 0

    for update in updates:
        sorted_update = sorted(update, key=cmp)
        if update != sorted_update:
            total += int(sorted_update[len(sorted_update) // 2])

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
