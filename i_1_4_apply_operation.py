# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Codercise I.1.4 — Applying a quantum operation.

Quantum operations are unitary matrices; the state after an operation is
|psi'> = U|psi>. Here U is the Hadamard matrix.
"""

import numpy as np

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


def apply_u(state):
    """Apply a quantum operation.

    Args:
        state (np.array[complex]): A normalized quantum state vector.

    Returns:
        np.array[complex]: The output state after applying U.
    """
    # APPLY U TO THE INPUT STATE AND RETURN THE NEW STATE
    return np.dot(U, state)


if __name__ == "__main__":
    ket_0 = np.array([1, 0])
    ket_1 = np.array([0, 1])

    print(f"U|0> = {apply_u(ket_0)}")
    print(f"U|1> = {apply_u(ket_1)}")
    print(f"U(U|0>) = {apply_u(apply_u(ket_0))}  (U is its own inverse)")
