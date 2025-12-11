"""
Advent of Code 2025 - Day 11 - Part 2
"""

from time import perf_counter
import networkx as nx
from functools import lru_cache


def read_input(filename="data.txt"):
    """Read and return the input data."""
    with open(filename, "r") as f:
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    lines = data.split("\n")

    G = nx.DiGraph()

    result = 0

    for line in lines:
        parts = line.split(": ")
        for edge in parts[1].split():
            G.add_edge(parts[0], edge)

    @lru_cache(maxsize=None)
    def count_paths(source, target):

        if source == target:
            return 1
        total = 0
        if source in G:
            for neighbour in G[source]:
                total += count_paths(neighbour, target)
        return total

    p1 = (
        count_paths("svr", "dac")
        * count_paths("dac", "fft")
        * count_paths("fft", "out")
    )
    p2 = (
        count_paths("svr", "fft")
        * count_paths("fft", "dac")
        * count_paths("dac", "out")
    )

    result = p1 + p2

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
