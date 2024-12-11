import time
from datetime import timedelta


def main():
    total = 0
    with open("day_02/data.txt") as f:
        for line in f:
            games = line.strip().split(": ")[1].split(";")
            max_g, max_r, max_b = 0, 0, 0
            for game in games:
                g, r, b = 0, 0, 0
                for go in game.strip().split(", "):
                    num, player = go.split(" ")
                    num = int(num)
                    if player == "green":
                        g += num
                    elif player == "blue":
                        b += num
                    elif player == "red":
                        r += num
                max_g = max(max_g, g)
                max_r = max(max_r, r)
                max_b = max(max_b, b)
            total += max_g * max_r * max_b

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
