# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=6)
estimation_wires = [0, 1, 2, 3]
target_wires = [4, 5]


def prepare_eigenvector_superposition(alpha, beta, gamma, delta):
    norm_squared = (
        np.abs(alpha) ** 2 + np.abs(beta) ** 2 + np.abs(gamma) ** 2 + np.abs(delta) ** 2
    )
    norm = np.sqrt(norm_squared)
    state = np.array([alpha / norm, beta / norm, gamma / norm, delta / norm])

    qp.MottonenStatePreparation(state, wires=target_wires)


@qp.qnode(dev)
def qpe(unitary):
    prepare_eigenvector_superposition(1, 1, 1, 1)

    qp.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )
    return qp.probs(wires=estimation_wires)


mystery_phase = 0.9375

if __name__ == "__main__":
    U = qp.CRX.compute_matrix(1 / 3)

    probs = qpe(U)
    print(probs)
