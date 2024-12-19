import time
from datetime import timedelta
from collections import deque


def main():
    available_towels = []
    valid_combinations = 0
    with open("day_19/data.txt") as f:
        available_towels = f.readline().strip().split(", ")

        for combo in f.readlines()[1:]:
            combo = combo.strip()
            queue = deque([(0, 0)])
            visited = set()
            possible = False

            while queue:
                idx, towels_used = queue.popleft()
                if idx == len(combo):
                    possible = True
                    break
                if (idx, towels_used) in visited:
                    continue
                visited.add((idx, towels_used))

                for towel in available_towels:
                    if combo[idx:].startswith(towel):
                        queue.append((idx + len(towel), towels_used + 1))

            if possible:
                valid_combinations += 1
    print(valid_combinations)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
