import time
from datetime import timedelta
from collections import Counter


def main():
    with open("day_01/data.txt") as f:
        numbers = [list(map(int, line.strip().split())) for line in f]

    list1, list2 = zip(*numbers)
    list1 = sorted(list1)
    occurences = Counter(list2)

    similarity_score = sum([n * occurences[n] for n in list1])

    print(similarity_score)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
