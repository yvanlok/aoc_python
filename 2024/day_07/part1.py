import time
from datetime import timedelta
from itertools import product


def generate_permutations(equation):
    parts = equation.split()
    operators = product("+*", repeat=len(parts) - 1)
    permutations = []

    for ops in operators:
        perm = parts[0]
        for part, op in zip(parts[1:], ops):
            perm = f"({perm}{op}{part})"
        permutations.append(perm)

    return permutations


def main():
    with open("day_07/data.txt") as f:
        equations = f.readlines()
    total = 0
    for equation in equations:
        result, numbers = equation.split(": ")
        result = int(result)
        permutations = generate_permutations(numbers.strip())

        for perm in permutations:
            try:
                calculated_result = eval(perm)
                if calculated_result == result:
                    total += calculated_result
                    break
            except Exception as e:
                print(f"Error evaluating {perm}: {e}")
    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
