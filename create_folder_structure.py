import os


def create_advent_of_code_structure(base_path, year):
    year_path = os.path.join(base_path, str(year))
    for day in range(1, 26):
        # Create day directory
        day_dir = os.path.join(year_path, f"day_{day:02}")
        os.makedirs(day_dir, exist_ok=True)

        # Create files inside the directory
        for filename in ["data.txt", "part1.py", "part2.py"]:
            file_path = os.path.join(day_dir, filename)
            open(file_path, "w").close()  # Create an empty file

    print(f"Advent of Code structure for {year} created in {year_path}")


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the base path for your Advent of Code project relative to the script directory
year = input("Enter the year for Advent of Code: ")
create_advent_of_code_structure(script_dir, year)
