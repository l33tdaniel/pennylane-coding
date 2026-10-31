# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from p_2_2_controlled_powers_of_u import apply_controlled_powers_of_U

dev = qp.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]


def prepare_eigenvector():
    qp.PauliX(wires=target_wires)


@qp.qnode(dev)
def qpe(unitary):
    prepare_eigenvector()

    for wire in estimation_wires:
        qp.Hadamard(wires=wire)

    apply_controlled_powers_of_U(unitary)

    qp.adjoint(qp.QFT)(wires=estimation_wires)

    return qp.probs(wires=estimation_wires)


if __name__ == "__main__":
    U = qp.T.compute_matrix()
    print(qpe(U))
