import time
from datetime import timedelta

def main():
    games = [{}]
    with open("day_13/data.txt") as f:
        for line in f:
            line = line.strip()
            if line != "":
                if line.startswith("Button A: "):
                    parts = line[10:].split(", ")
                    games[-1]["A"] = (int(parts[0][2:]), int(parts[1][2:]))
                elif line.startswith("Button B: "):
                    parts = line[10:].split(", ")
                    games[-1]["B"] = (int(parts[0][2:]), int(parts[1][2:]))
                elif line.startswith("Prize: "):
                    parts = line[7:].split(", ")
                    games[-1]["Prize"] = (int(parts[0][2:]), int(parts[1][2:]))
            else:
                games.append({})

    tokens = 0

    for game in games:
        x, y = game["Prize"]
        xa, ya = game["A"]
        xb, yb = game["B"]
       

        # Try all possible combinations of a (Button A presses) and b (Button B presses)
        for a in range(0, min(100, (x // xa) + 1)):
            for b in range(0, min(100, (y // yb) + 1)):
                # Check if the total movement in the X and Y direction matches the prize location
                if (a * xa + b * xb == x) and (a * ya + b * yb == y):
                    cost = a * 3 + b * 1  # 3 tokens for Button A, 1 token for Button B
                    tokens += cost
                    break
                    
    print(tokens)
if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
