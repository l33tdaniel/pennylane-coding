# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def create_one_minus():
    qp.PauliX(wires=0)
    qp.PauliX(wires=1)
    qp.Hadamard(wires=1)

    return qp.expval(qp.PauliZ(0) @ qp.PauliX(1))


if __name__ == "__main__":
    print(create_one_minus())
