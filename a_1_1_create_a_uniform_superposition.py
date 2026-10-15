# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)


@qp.qnode(dev)
def naive_circuit():
    for wire in range(n_bits):
        qp.Hadamard(wires=wire)

    return qp.probs(wires=range(n_bits))


if __name__ == "__main__":
    print(naive_circuit())
