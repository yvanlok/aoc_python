import time
from datetime import timedelta


def addition(gates):
    gates_with_x = [gate for gate in gates if gate.startswith("x")]
    gates_with_y = [gate for gate in gates if gate.startswith("y")]
    gates_with_z = [gate for gate in gates if gate.startswith("z")]

    gates_with_x = sorted(gates_with_x, key=lambda x: int(x[1:]), reverse=True)
    gates_with_y = sorted(gates_with_y, key=lambda x: int(x[1:]), reverse=True)
    gates_with_z = sorted(gates_with_z, key=lambda x: int(x[1:]), reverse=True)

    final_num_x = int("".join(str(gates[g]) for g in gates_with_x), 2)
    final_num_y = int("".join(str(gates[g]) for g in gates_with_y), 2)
    final_num_z = int("".join(str(gates[g]) for g in gates_with_z), 2)

    return (final_num_x, final_num_y, final_num_x + final_num_y, final_num_z)


def main():

    gates = {}
    operations = []
    highest_z = "z00"

    with open("day_24/data.txt") as f:
        for line in f.readlines():
            if ":" in line:
                gate, value = line.strip().split(": ")
                gates[gate] = int(value)
            elif line.strip() != "":
                op1, op, op2, _, res = line.strip().split(" ")
                operations.append((op1, op, op2, res))
                if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
                    highest_z = res
    wrong = set()

    for op1, op, op2, res in operations:
        if res[0] == "z" and op != "XOR" and res != highest_z:
            wrong.add(res)
        if (
            op == "XOR"
            and res[0] not in ["x", "y", "z"]
            and op1[0] not in ["x", "y", "z"]
            and op2[0] not in ["x", "y", "z"]
        ):
            wrong.add(res)
        if op == "AND" and "x00" not in [op1, op2]:
            for subop1, subop, subop2, subres in operations:
                if (res == subop1 or res == subop2) and subop != "OR":
                    wrong.add(res)
        if op == "XOR":
            for subop1, subop, subop2, subres in operations:
                if (res == subop1 or res == subop2) and subop == "OR":
                    wrong.add(res)
    print(",".join(sorted(list(wrong))))


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
