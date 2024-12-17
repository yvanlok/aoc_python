import time
from datetime import timedelta


def fetch_value(operand, a, b, c):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    return None


def main():
    instruction_pointer = 0
    instructions = []
    outputs = []
    A, B, C = None, None, None

    with open("day_17/data.txt") as f:
        full_string = "".join(f.readlines())
        parts = full_string.split("\n\n")
        A, B, C = [int(line.split(": ")[1]) for line in parts[0].splitlines()]
        instructions = list(map(int, parts[1].split(": ")[1].split(",")))

    while instruction_pointer < len(instructions):
        # Ensure we can read the operand
        if instruction_pointer + 1 >= len(instructions):
            break

        opcode = instructions[instruction_pointer]
        literal_operand = instructions[instruction_pointer + 1]
        combo_operand = fetch_value(literal_operand, A, B, C)

        if opcode == 0:
            A = A // 2**combo_operand
            instruction_pointer += 2
        elif opcode == 1:
            B = B ^ literal_operand
            instruction_pointer += 2
        elif opcode == 2:
            B = combo_operand % 8
            instruction_pointer += 2
        elif opcode == 3:
            if A != 0:
                instruction_pointer = literal_operand
            else:
                instruction_pointer += 2
        elif opcode == 4:
            B = B ^ C
            instruction_pointer += 2
        elif opcode == 5:
            outputs.append(combo_operand % 8)
            instruction_pointer += 2
        elif opcode == 6:
            B = A // 2**combo_operand
            instruction_pointer += 2
        elif opcode == 7:
            C = A // 2**combo_operand
            instruction_pointer += 2
        else:
            instruction_pointer += 2

    print(",".join(map(str, outputs)))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Time taken: {timedelta(seconds=end_time - start_time)}")
