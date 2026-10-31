# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

from p_3_1_sampling_for_the_phase import phase_window, qpe

dev = qp.device("default.qubit", wires=10)


def estimates_array(unitary):
    estimates = []
    target_wires = [9]

    for num_estimation_wires in range(2, 10):
        estimation_wires = range(0, num_estimation_wires)
        probs = qpe(unitary, estimation_wires, target_wires)
        estimates.append(phase_window(probs, estimation_wires))

    return estimates


if __name__ == "__main__":
    U = np.array([[1, 0], [0, np.exp((2 * np.pi * 1j / 7))]])

    for n, window in zip(range(2, 10), estimates_array(U)):
        print(n, window)
