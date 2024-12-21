import time
from datetime import timedelta
from collections import deque
from itertools import product
from functools import cache


def compute_seqs(keypad):
    pos = {}

    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)
    seqs = {}

    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            else:
                possibilities = []
                q = deque([(pos[x], "")])
                optimal = float("inf")

                while q:
                    (r, c), moves = q.popleft()
                    for nr, nc, nm in [
                        (r - 1, c, "^"),
                        (r + 1, c, "v"),
                        (r, c - 1, "<"),
                        (r, c + 1, ">"),
                    ]:
                        if (
                            nr < 0
                            or nr >= len(keypad)
                            or nc < 0
                            or nc >= len(keypad[0])
                        ):
                            continue
                        if keypad[nr][nc] is None:
                            continue
                        if keypad[nr][nc] == y:
                            if optimal < len(moves) + 1:
                                break
                            else:
                                optimal = len(moves) + 1
                                possibilities.append(moves + nm + "A")
                        else:
                            q.append(((nr, nc), moves + nm))
                    else:
                        continue
                    break

                seqs[(x, y)] = possibilities
    return seqs


num_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]
num_seqs = compute_seqs(num_keypad)

dir_keypad = [[None, "^", "A"], ["<", "v", ">"]]
dir_seqs = compute_seqs(dir_keypad)
dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}


@cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(compute_length(subseq, depth - 1) for subseq in dir_seqs[(x, y)])
    return length


def solve(string, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]


def main():

    with open("day_21/data.txt") as f:
        codes = [line.strip() for line in f]

    total = 0

    for code in codes:
        inputs = solve(code, num_seqs)
        total += min(map(compute_length, inputs)) * int(code[:-1])

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
