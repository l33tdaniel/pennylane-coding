# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def guess_the_unitary(unitary):
    qp.Hadamard(wires=0)
    qp.ctrl(qp.QubitUnitary(unitary, wires=1), control=0)
    qp.Hadamard(wires=0)

    return qp.probs(wires=0)


if __name__ == "__main__":
    U = qp.PauliZ.compute_matrix()

    # U = (-1)*qp.PauliZ.compute_matrix()

    print(guess_the_unitary(U))
