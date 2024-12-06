import time
from datetime import timedelta


def main():
    with open("day_05/data.txt") as f:
        ordering_rules, updates = "".join(f.readlines()).split("\n\n")
        ordering_rules = [line.split("|") for line in ordering_rules.splitlines()]
        updates = [line.split(",") for line in updates.splitlines()]

    total = 0

    for update in updates:

        if determine_validity(update, ordering_rules):
            total += int(update[len(update) // 2])
    print(total)


def determine_validity(update, ordering_rules):
    for i in range(len(update)):
        for j in range(i, len(update)):
            for rule in ordering_rules:
                if update[i] == rule[1] and update[j] == rule[0]:
                    return False
    return True


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
