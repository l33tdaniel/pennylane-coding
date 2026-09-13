# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def two_qubit_circuit():
    qp.Hadamard(wires=0)
    qp.PauliX(wires=1)

    return qp.expval(qp.PauliY(0)), qp.expval(qp.PauliZ(1))


if __name__ == "__main__":
    print(two_qubit_circuit())
