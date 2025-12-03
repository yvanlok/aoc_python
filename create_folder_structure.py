import os


def create_advent_of_code_structure(base_path, year):
    year_path = os.path.join(base_path, str(year))

    # Read the base template file
    base_template_path = os.path.join(base_path, "base_file.py")
    with open(base_template_path, "r") as f:
        template = f.read()

    for day in range(1, 13):  # Changed to 13 for 12 days
        # Create day directory
        day_dir = os.path.join(year_path, f"day_{day:02}")
        os.makedirs(day_dir, exist_ok=True)

        # Create data.txt (only if it doesn't exist)
        data_path = os.path.join(day_dir, "data.txt")
        if not os.path.exists(data_path):
            open(data_path, "w").close()

        # Create part1.py with template (only if it doesn't exist)
        part1_path = os.path.join(day_dir, "part1.py")
        if not os.path.exists(part1_path):
            with open(part1_path, "w") as f:
                f.write(template.format(year=year, day=day, part=1))

        # Create part2.py with template (only if it doesn't exist)
        part2_path = os.path.join(day_dir, "part2.py")
        if not os.path.exists(part2_path):
            with open(part2_path, "w") as f:
                f.write(template.format(year=year, day=day, part=2))

    print(f"Advent of Code structure for {year} created in {year_path}")
    print(f"Created 12 days with boilerplate templates from base_file.py")


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the base path for your Advent of Code project relative to the script directory
year = input("Enter the year for Advent of Code: ")
create_advent_of_code_structure(script_dir, year)
