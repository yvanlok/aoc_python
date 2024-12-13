import time
from datetime import timedelta


def solve_equation(p_x, p_y, xa, ya, xb, yb, offset):
    # Apply the offset to the prize coordinates
    p_x += offset
    p_y += offset
    
    # Calculate the determinant
    det = xa * yb - ya * xb

    # Ensure that the determinant is non-zero
    if det == 0:
        return 0

    # Calculate a and b values based on the formula
    a = (p_x * yb - p_y * xb) / det
    b = (p_y * xa - p_x * ya) / det

    # Check if a and b are integers
    if a.is_integer() and b.is_integer():
        a = int(a)
        b = int(b)
        # Check if the solution satisfies the original equation
        if (xa * a + xb * b == p_x) and (ya * a + yb * b == p_y):
            return a * 3 + b
    return 0


def main():
    games = []
    offset = 10000000000000
    # offset = 0
    with open("day_13/data.txt") as f:
        game = {}
        for line in f:
            line = line.strip()
            if line != "":
                if line.startswith("Button A: "):
                    parts = line[10:].split(", ")
                    game["A"] = (int(parts[0][2:]), int(parts[1][2:]))
                elif line.startswith("Button B: "):
                    parts = line[10:].split(", ")
                    game["B"] = (int(parts[0][2:]), int(parts[1][2:]))
                elif line.startswith("Prize: "):
                    parts = line[7:].split(", ")
                    game["Prize"] = (int(parts[0][2:]), int(parts[1][2:]))
            else:
                games.append(game)
                game = {}  # reset for next game

        # Append the last game if the file doesn't end with a blank line
        if game:
            games.append(game)

    tokens = 0

    for game in games:
        p_x, p_y = game["Prize"]
        xa, ya = game["A"]
        xb, yb = game["B"]
        
        tokens += solve_equation(p_x, p_y, xa, ya, xb, yb, offset)

    print(int(tokens))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
