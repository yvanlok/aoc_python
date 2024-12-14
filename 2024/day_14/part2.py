import time
from datetime import timedelta


def final_position(robot, width=101, height=103):
    pos = robot["position"]
    velocity = robot["velocity"]

    pos = (pos[0] + velocity[0], pos[1] + velocity[1])
    pos = (pos[0] % (width), pos[1] % (height))
    return {"position": pos, "velocity": velocity}


def print_grid(robots, width, height):
    grid = [["." for _ in range(width)] for _ in range(height)]
    for robot in robots:
        x, y = robot["position"]
        grid[y][x] = "#"
    for row in grid:
        print("".join(row))
    print("\n" + "-" * width + "\n")


def main():
    width = 101
    height = 103
    robots = []
    with open("day_14/data.txt") as f:
        for line in f.readlines():
            parts = line.strip().split(" ")
            position = tuple(map(int, parts[0][2:].split(",")))
            velocity = tuple(map(int, parts[1][2:].split(",")))
            robot = {
                "position": position,
                "velocity": velocity,
            }
            robots.append(robot)
    final_positions = []
    next_robots = []
    iterations = 1
    while True:
        for robot in robots:
            new_robot = final_position(robot, width=width, height=height)
            final_positions.append(new_robot)
            next_robots.append(new_robot)
        robots = next_robots
        next_robots = []
        positions = [robot["position"] for robot in final_positions]
        if len(positions) == len(set(positions)):
            print(f"Iteration {iterations}: All positions are unique")
            print_grid(final_positions, width, height)
        final_positions.clear()
        iterations += 1


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
