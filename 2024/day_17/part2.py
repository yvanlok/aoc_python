import time
from datetime import timedelta
from dataclasses import dataclass
from math import trunc


@dataclass
class State:
    A: int
    B: int
    C: int
    ip: int


def fetch_value(state, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return state.A
    elif operand == 5:
        return state.B
    elif operand == 6:
        return state.C
    return None


def next_instruction(state, instructions):
    """Execute the next instruction and update the state."""
    output = None
    opcode = instructions[state.ip]
    operand = instructions[state.ip + 1]
    value = fetch_value(state, operand)

    if opcode == 0:  # adv
        state.A = trunc(state.A / (2**value))
    elif opcode == 1:  # bxl
        state.B = state.B ^ operand
    elif opcode == 2:  # bst
        state.B = value % 8
    elif opcode == 3:  # jnz
        if state.A != 0:
            state.ip = operand
            return state, output
    elif opcode == 4:  # bxc
        state.B = state.B ^ state.C
    elif opcode == 5:  # out
        output = value % 8
    elif opcode == 6:  # bdv
        state.B = trunc(state.A / (2**value))
    elif opcode == 7:  # cdv
        state.C = trunc(state.A / (2**value))

    state.ip += 2
    return state, output


def run_program(state, instructions):
    """Run the program starting from the given state. Return outputs."""
    outputs = []
    while state.ip < len(instructions):
        state, output = next_instruction(state, instructions)
        if output is not None:
            outputs.append(output)
    return outputs


def search(instructions):
    """Find the value of A such that the program outputs itself."""
    a = 0
    reversed_prog = instructions.copy()
    reversed_prog.reverse()
    N = len(instructions)

    for i in range(N):
        target_suffix = instructions[N - i - 1 :]
        t = 0
        while True:
            candidate_a = (a << 3) + t  # Shift and add to get new A
            state = State(candidate_a, 0, 0, 0)
            result = run_program(state, instructions)
            if result == target_suffix:
                a = candidate_a
                break
            t += 1
    return a


def main():
    with open("day_17/data.txt") as f:
        full_string = f.read().strip()
        parts = full_string.split("\n\n")
        A, B, C = [int(line.split(": ")[1]) for line in parts[0].splitlines()]
        instructions = list(map(int, parts[1].split(": ")[1].split(",")))

    # Find the correct initial A value
    result = search(instructions)
    print(result)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Time taken: {timedelta(seconds=end_time - start_time)}")
