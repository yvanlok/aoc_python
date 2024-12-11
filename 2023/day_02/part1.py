from datetime import timedelta
import time


def is_game_possible(game):
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
    return r <= 12 and g <= 13 and b <= 14


def main():
    total = 0
    with open("day_02/data.txt") as f:
        for idx, line in enumerate(f):
            games = line.strip().split(": ")[1].split(";")
            if all(is_game_possible(game) for game in games):
                total += idx + 1
    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
