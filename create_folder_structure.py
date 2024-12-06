import os


def create_advent_of_code_structure(base_path):
    for day in range(1, 26):
        # Create day directory
        day_dir = os.path.join(base_path, f"day_{day:02}")
        os.makedirs(day_dir, exist_ok=True)

        # Create files inside the directory
        for filename in ["data.txt", "part1.py", "part2.py"]:
            file_path = os.path.join(day_dir, filename)
            open(file_path, "w").close()  # Create an empty file

    print(f"Advent of Code structure created in {base_path}")


# Set the base path for your Advent of Code project
base_path = r"E:\Projects\Python\Advent of COde\2024"
create_advent_of_code_structure(base_path)
