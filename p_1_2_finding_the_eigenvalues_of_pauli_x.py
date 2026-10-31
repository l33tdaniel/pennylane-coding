# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def phase_kickback_X(eigenvector):
    if eigenvector == "minus":
        qp.PauliX(wires=1)
    qp.Hadamard(wires=1)

    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])
    qp.Hadamard(wires=0)

    return qp.probs(wires=[0])


eigenvalue_of_X_plus = 1
eigenvalue_of_X_minus = -1

done = True

if __name__ == "__main__":
    print(phase_kickback_X("plus"))
    print(phase_kickback_X("minus"))
