# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_h_and_measure(state):
    if state == 1:
        qp.PauliX(wires=0)

    qp.Hadamard(wires=0)

    return qp.probs(wires=0)


if __name__ == "__main__":
    print(apply_h_and_measure(0))
    print(apply_h_and_measure(1))
