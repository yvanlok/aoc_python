"""
Advent of Code 2025 - Day 10 - Part 1
"""

from time import perf_counter
from collections import deque


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    diagrams = []
    button_masks = []
    # joltages = [] # probably in part 2

    result = 0

    for line in lines:

        parts = line.split()
        diagram = parts[0][1:-1]
        wiring = parts[1:-1]

        diagrams.append(diagram)

        line_button_masks = []

        for button in wiring:

            button = button[1:-1].split(",")
            button_mask = list("." * len(diagram))

            for i in button:
                button_mask[int(i)] = "#"

            line_button_masks.append("".join(button_mask))

        button_masks.append(line_button_masks)

    for idx in range(0, len(diagrams)):
        queue = deque()
        queue.append(
            ("." * len(diagrams[idx]), 0)
        )  # (empty diagram, button presses) = 0
        visited = set()
        visited.add("." * len(diagrams[0]))  # don't repeat

        while queue:
            current = queue.popleft()
            (mask, number) = current

            # check if diagram has been reached
            if mask == diagrams[idx]:
                result += number
                break
            else:
                # add each possible next mask to queue
                for next_mask in button_masks[idx]:
                    resultant_mask = xor_strings(mask, next_mask)
                    # only add if not visited so far
                    if resultant_mask not in visited:
                        visited.add(resultant_mask)
                        queue.append((resultant_mask, number + 1))

    return result


def xor_strings(s1, s2):
    return "".join("#" if c1 != c2 else "." for c1, c2 in zip(s1, s2))


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
