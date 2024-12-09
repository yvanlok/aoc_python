import time
from datetime import timedelta


def main():

    file_system = []

    # Read input
    with open("day_09/data.txt") as f:
        for idx, c in enumerate(f.readline().strip()):
            if idx % 2 == 0:
                file_id = idx // 2
                file_system.extend([str(file_id)] * int(c))
            else:
                file_system.extend(["."] * int(c))

    # Start compacting process
    for i in range(len(file_system)):
        if file_system[i] == ".":
            last_index = last_file_index(file_system)
            if file_system[last_index] != ".":
                # Move the block to the free space
                file_system[i] = file_system[last_index]
                file_system[last_index] = "."

        # If we reached a point where there are no more files to move
        if all(x == "." for x in file_system[i + 1 :]):
            break

    # Calculate checksum
    checksum = 0
    for idx, file in enumerate(file_system):
        if file != ".":
            checksum += int(file) * idx

    # Print the final checksum
    print(f"Checksum: {checksum}")


def last_file_index(file_system):
    for i in range(len(file_system) - 1, -1, -1):
        if file_system[i] != ".":
            return i


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
