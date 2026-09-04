# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Codercise I.1.3 — Sampling measurement outcomes.

Simulate measuring a single-qubit state num_meas times, returning samples of
0 or 1 drawn from the probability distribution |<0|psi>|^2, |<1|psi>|^2.
"""

import numpy as np


def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (np.array[complex]): A normalized qubit state vector.
        num_meas (int): The number of measurements to take

    Returns:
        np.array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability
        distribution defined by the input state.
    """
    # COMPUTE THE MEASUREMENT OUTCOME PROBABILITIES
    probs = np.abs(state) ** 2

    # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES
    return np.random.choice([0, 1], size=num_meas, p=probs)


if __name__ == "__main__":
    state = np.array([0.8, 0.6])  # 64% |0>, 36% |1>
    samples = measure_state(state, 100)
    print(samples)
    print(f"fraction of 1s: {np.mean(samples):.2f} (expected ~0.36)")
