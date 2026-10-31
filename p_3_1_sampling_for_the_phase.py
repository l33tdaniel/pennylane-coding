# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=10)


@qp.qnode(dev)
def qpe(unitary, estimation_wires, target_wires):
    qp.PauliX(wires=target_wires)

    qp.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )

    return qp.probs(wires=estimation_wires)


def fractional_binary_to_decimal(binary_fraction, wires):
    return float(binary_fraction / 2 ** len(wires))


def phase_window(probs, estimation_wires):
    first, second = np.argsort(probs)[::-1][:2]

    bound_1 = fractional_binary_to_decimal(first, estimation_wires)
    bound_2 = fractional_binary_to_decimal(second, estimation_wires)
    return (bound_1, bound_2)


done = True

if __name__ == "__main__":
    estimation_wires = range(0, 3)

    target_wires = [9]

    U = np.array([[1, 0], [0, np.exp((2 * np.pi * 1j / 7))]])

    probs = qpe(U, estimation_wires, target_wires)

    print(phase_window(probs, estimation_wires))
