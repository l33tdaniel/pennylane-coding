# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qp.device("default.qubit", wires=all_wires)


def oracle(combo):
    combo_str = "".join(str(j) for j in combo)

    qp.MultiControlledX(wires=all_wires, control_values=combo)


if __name__ == "__main__":
    print(qp.draw(oracle)([1, 0, 1, 0, 0]))
