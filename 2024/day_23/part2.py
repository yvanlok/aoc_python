import time
from datetime import timedelta
from collections import deque


def main():
    connections = {}
    with open("day_23/data.txt") as f:
        for line in f:
            c1, c2 = line.strip().split("-")
            connections.setdefault(c1, []).append(c2)
            connections.setdefault(c2, []).append(c1)

    visited_sets = []
    seen_global = set()

    for start in connections:
        if start in seen_global:
            continue
        # Standard BFS
        q = deque([start])
        visited = {start}
        while q:
            current = q.popleft()
            for nxt in connections[current]:
                if all(nxt in connections[v] for v in visited):
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

        visited_sets.append(sorted(visited))
        seen_global.update(visited)

    largest = max(visited_sets, key=len)
    print(",".join(largest))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
