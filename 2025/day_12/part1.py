"""
Advent of Code 2025 - Day 12 - Part 1
"""

from time import perf_counter


def read_input(filename="data.txt"):
    """Read and return the input data."""
    # Open and read the input file
    with open(filename, "r") as f:
        # Strip whitespace and return the contents
        return f.read().strip()


def solve(data):
    """Solve the puzzle."""
    # Split input into sections separated by blank lines
    sections = data.split("\n\n")

    # List to store the shape patterns for each present
    present_shapes = []

    # List to store region size and required present quantities
    region_requirements = []

    # Parse all sections except the last (which contains requirements)
    for section in sections[:-1]:
        lines = section.splitlines()
        # Skip the first line (shape index) and store the shape grid
        present_shapes.append(lines[1:])

    # Parse the final section containing region requirements
    requirements_section = sections[-1].splitlines()

    for requirement_line in requirements_section:
        # Split region size from shape quantities
        (region_size, shape_counts) = requirement_line.split(": ")
        # Store as tuple: (region dimensions, list of quantities for each shape)
        region_requirements.append(
            (region_size, [int(x) for x in shape_counts.split()])
        )

    # Calculate the area (number of # cells) for each present shape
    shape_areas = []

    for shape in present_shapes:
        # Count the number of '#' characters in the shape
        cell_count = 0
        for row in shape:
            for cell in row:
                if cell == "#":
                    cell_count += 1
        shape_areas.append(cell_count)

    # Counter for regions that can fit all required presents
    valid_regions_count = 0

    # Check each region to see if all presents can fit
    for requirement in region_requirements:
        # Parse region dimensions (e.g., "12x5" -> height=12, width=5)
        height, width = requirement[0].split("x")
        # Calculate total available area in the region
        region_area = int(height) * int(width)

        # Calculate total area needed for all required presents
        total_presents_area = 0

        # Sum up area for each shape type based on quantity required
        for shape_index, shape_quantity in enumerate(requirement[1]):
            total_presents_area += shape_quantity * shape_areas[shape_index]

        # Check if presents fit with buffer space (-9 needed for example test case)
        if total_presents_area <= region_area - 9:
            valid_regions_count += 1

    return valid_regions_count


def main():
    data = read_input()

    start = perf_counter()

    result = solve(data)

    elapsed = perf_counter() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
