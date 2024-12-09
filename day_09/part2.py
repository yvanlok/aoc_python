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

    # Identify free spaces
    free_spaces = []
    i = 0
    while i < len(file_system):
        if file_system[i] == ".":
            start = i
            while i < len(file_system) and file_system[i] == ".":
                i += 1
            free_spaces.append({"start": start, "end": i - 1, "length": i - start})
        else:
            i += 1

    # Identify files
    files = []
    i = 0
    while i < len(file_system):
        if file_system[i] != ".":
            file_id = file_system[i]
            start = i
            while i < len(file_system) and file_system[i] == file_id:
                i += 1
            files.append(
                {"id": file_id, "start": start, "end": i - 1, "length": i - start}
            )
        else:
            i += 1

    # Sort files by ID (descending)
    files.sort(key=lambda x: int(x["id"]), reverse=True)

    # Compact files
    for file in files:
        for free_space in free_spaces:
            if (
                free_space["length"] >= file["length"]
                and free_space["start"] < file["start"]
            ):
                # Move file to the leftmost suitable free space
                for i in range(file["length"]):
                    file_system[free_space["start"] + i] = file["id"]
                    file_system[file["start"] + i] = "."

                # Update free space
                free_space["start"] += file["length"]
                free_space["length"] -= file["length"]
                break

    # Compute checksum
    checksum = sum(
        int(file_system[i]) * i
        for i in range(len(file_system))
        if file_system[i] != "."
    )
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
