import time
from datetime import timedelta


def main():

    connections = {}

    with open("day_23/data.txt") as f:
        for line in f.readlines():
            comp1, comp2 = line.strip().split("-")
            if comp1 in connections:
                connections[comp1] += [comp2]
            else:
                connections[comp1] = [comp2]

            if comp2 in connections:
                connections[comp2] += [comp1]
            else:
                connections[comp2] = [comp1]

    sets = []
    for key in connections.keys():
        if key.startswith("t"):
            for comp1 in connections[key]:
                for comp2 in connections.get(comp1, []):
                    if comp2 in connections.get(key, []) and comp2 not in [key, comp1]:
                        keys = (key, comp1, comp2)
                        sets.append(keys)

    unique_sets = set(tuple(sorted(s)) for s in sets)
    total = len(unique_sets)

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
