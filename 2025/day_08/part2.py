"""
Advent of Code 2025 - Day 8 - Part 2
"""

from time import perf_counter
import math


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    positions = [[int(x) for x in line.split(",")] for line in lines]

    circuits = [[i] for i in range(0, len(positions))]

    distances = {}

    for i in range(0, len(positions)):
        for j in range(i + 1, len(positions)):
            distances[(i, j)] = math.dist(positions[i], positions[j])

    sorted_distances = sorted(distances.items(), key=lambda x: x[1])

    i = 0

    final_connection = None

    while len(circuits) > 1:
        (box_1, box_2), distance = sorted_distances[i]

        # Find the circuits that box_1 and box_2 belong to
        circuit_1 = next(circuit for circuit in circuits if box_1 in circuit)
        circuit_2 = next(circuit for circuit in circuits if box_2 in circuit)

        # If they are in different circuits, merge them
        if circuit_1 != circuit_2:
            circuits.remove(circuit_1)
            circuits.remove(circuit_2)
            circuits.append(circuit_1 + circuit_2)

            # Check if this was the final merge
            if len(circuits) == 1:
                final_connection = (box_1, box_2)
                break

        i += 1

    # Calculate result based on the final connection
    result = positions[final_connection[0]][0] * positions[final_connection[1]][0]

    return result


def main():
    data = read_input()

    start = perf_counter()
    result = solve(data)
    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
