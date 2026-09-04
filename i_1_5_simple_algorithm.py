# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Codercise I.1.5 — A simple quantum algorithm.

A minimal single-qubit simulator:
  1. Initialize a qubit in state |0>
  2. Apply the provided operation U (Hadamard)
  3. Simulate measuring the output state 100 times
"""

import numpy as np

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


def initialize_state():
    """Prepare a qubit in state |0>.

    Returns:
        np.array[float]: the vector representation of state |0>.
    """
    # PREPARE THE STATE |0>
    return np.array([1, 0])


def apply_u(state):
    """Apply a quantum operation."""
    return np.dot(U, state)


def measure_state(state, num_meas):
    """Measure a quantum state num_meas times."""
    p_alpha = np.abs(state[0]) ** 2
    p_beta = np.abs(state[1]) ** 2
    meas_outcome = np.random.choice([0, 1], p=[p_alpha, p_beta], size=num_meas)
    return meas_outcome


def quantum_algorithm():
    """Use the functions above to implement the quantum algorithm described above.

    Try and do so using three lines of code or less!

    Returns:
        np.array[int]: the measurement results after running the algorithm 100 times
    """
    # PREPARE THE STATE, APPLY U, THEN TAKE 100 MEASUREMENT SAMPLES
    return measure_state(apply_u(initialize_state()), 100)


if __name__ == "__main__":
    results = quantum_algorithm()
    print(results)
    print(f"fraction of 1s: {np.mean(results):.2f} (expected ~0.50)")
