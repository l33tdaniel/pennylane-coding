# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

from p_2_3_the_full_qpe_circuit import qpe

estimation_wires = [0, 1, 2]
target_wires = [3]


def estimate_phase(probs):
    most_likely = np.argmax(probs)

    return most_likely / 2 ** len(estimation_wires)


if __name__ == "__main__":
    U = qp.T.compute_matrix()

    probs = qpe(U)

    estimated_phase = estimate_phase(probs)
    print(estimated_phase)
