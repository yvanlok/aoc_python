import time
from datetime import timedelta
from functools import reduce
import operator


def final_position(robot, time=100, width=101, height=103):
    pos = robot["position"]
    velocity = robot["velocity"]
    for i in range(0, 100):
        pos = (pos[0] + velocity[0], pos[1] + velocity[1])
        pos = (pos[0] % (width), pos[1] % (height))
    return pos


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

    for robot in robots:
        final_positions.append(
            final_position(robot, time=100, width=width, height=height)
        )

    quadrants = [0, 0, 0, 0]  # Quadrants I, II, III, IV

    for pos in final_positions:
        if pos[0] > width // 2 and pos[1] > height // 2:
            quadrants[0] += 1  # Quadrant I
        elif pos[0] < width // 2 and pos[1] > height // 2:
            quadrants[1] += 1  # Quadrant II
        elif pos[0] < width // 2 and pos[1] < height // 2:
            quadrants[2] += 1  # Quadrant III
        elif pos[0] > width // 2 and pos[1] < height // 2:
            quadrants[3] += 1  # Quadrant IV

    quadrant_product = reduce(operator.mul, quadrants, 1)
    print(f"Product of all numbers in quadrants: {quadrant_product}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
