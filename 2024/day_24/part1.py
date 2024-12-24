import time
from datetime import timedelta


def main():

    gates = {}
    operations = []
    with open("day_24/data.txt") as f:
        for line in f.readlines():
            if ":" in line:
                gate, value = line.strip().split(": ")
                gates[gate] = int(value)
            elif line.strip() != "":
                parts = line.strip().split(" ")
                operations.append(
                    {
                        "gate1": parts[0],
                        "gate2": parts[2],
                        "operation": parts[1],
                        "final_gate": parts[4],
                    }
                )

    idx = 0
    while idx < len(operations):
        op = operations[idx]
        gate1, gate2, operation, final_gate = (
            op["gate1"],
            op["gate2"],
            op["operation"],
            op["final_gate"],
        )
        if gate1 in gates and gate2 in gates:
            if operation == "XOR":
                final_value = gates[gate1] ^ gates[gate2]
            elif operation == "AND":
                final_value = gates[gate1] & gates[gate2]
            elif operation == "OR":
                final_value = gates[gate1] | gates[gate2]

            gates[final_gate] = final_value

        if idx == len(operations) - 1:
            final_gates_with_z = [
                op["final_gate"]
                for op in operations
                if op["final_gate"].startswith("z")
            ]
            gates_with_z = [gate for gate in gates if gate.startswith("z")]

            if len(final_gates_with_z) == len(gates_with_z):
                gates_with_z = sorted(
                    gates_with_z, key=lambda x: int(x[1:]), reverse=True
                )
                final_num = ""
                for g in gates_with_z:
                    final_num += str(gates[g])
                print(int(final_num, 2))
                break

            idx = 0
        else:
            idx += 1


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print(f"Time taken: {elapsed_time}")
