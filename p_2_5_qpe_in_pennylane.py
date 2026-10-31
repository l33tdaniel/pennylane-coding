# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from p_2_4_computing_the_phase import estimate_phase

dev = qp.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]


def prepare_eigenvector():
    qp.PauliX(wires=target_wires)


@qp.qnode(dev)
def qpe(unitary):
    prepare_eigenvector()

    qp.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )

    return qp.probs(wires=estimation_wires)


if __name__ == "__main__":
    U = qp.T.compute_matrix()
    probs = qpe(U)
    print(estimate_phase(probs))
